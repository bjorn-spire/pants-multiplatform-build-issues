This is a test repository to showcase an issue where if you have binaries
that are forced to only be built for one platform hinders the tests to
run on another platform.

To trigger this issue run the following on a Mac:

```shell
$ ./pants test src/python::
```


The setup is as follows in `src/python/BUILD`:

1. library: depends on compiled dependency `bitarray`
2. test: runs on any platform and, well, runs tests
3. library-bin: A fake compiled binary with a hard-coded platform of Linux

Without the specified platform in `library-bin` the test runs fine.
One thing to note is that I have a `linux` packaged version of
`cffi` so when I look at the packages available I see that
package but Pants doesn't compile the Mac version as it should, I'm
guessing that is because it finds a version but it's the wrong one.

Run log:
```shell
% ./pants test src/python/::

19:09:15 00:00 [main]
               (To run a reporting server: ./pants server)
19:09:15 00:00   [setup]
19:09:16 00:01     [parse]
               Executing tasks in goals: bootstrap -> imports -> unpack-jars -> unpack-wheels -> deferred-sources -> native-compile -> link -> jvm-platform-validate -> gen -> resolve -> pyprep -> compile -> resources -> test
19:09:16 00:01   [bootstrap]
19:09:16 00:01     [substitute-aliased-targets]
19:09:16 00:01     [jar-dependency-management]
19:09:16 00:01     [bootstrap-jvm-tools]
19:09:16 00:01     [provide-tools-jar]
19:09:16 00:01   [imports]
19:09:16 00:01     [ivy-imports]
19:09:16 00:01   [unpack-jars]
19:09:16 00:01     [unpack-jars]
19:09:16 00:01   [unpack-wheels]
19:09:16 00:01     [unpack-wheels]
19:09:16 00:01   [deferred-sources]
19:09:16 00:01     [deferred-sources]
19:09:16 00:01   [native-compile]
19:09:16 00:01     [conan-prep]
19:09:17 00:02     [conan-fetch]
19:09:17 00:02     [c-for-ctypes]
19:09:17 00:02     [cpp-for-ctypes]
19:09:17 00:02   [link]
19:09:17 00:02     [shared-libraries]
19:09:17 00:02   [jvm-platform-validate]
19:09:17 00:02     [jvm-platform-validate]
19:09:17 00:02   [gen]
19:09:17 00:02     [antlr-java]
19:09:17 00:02     [antlr-py]
19:09:17 00:02     [jaxb]
19:09:17 00:02     [protoc]
19:09:17 00:02     [ragel]
19:09:17 00:02     [thrift-java]
19:09:17 00:02     [thrift-py]
19:09:17 00:02     [grpcio-prep]
19:09:17 00:02     [grpcio-run]
19:09:17 00:02     [wire]
19:09:17 00:02   [resolve]
19:09:17 00:02     [ivy]
19:09:17 00:02     [coursier]
19:09:17 00:02   [pyprep]
19:09:17 00:02     [interpreter]
19:09:17 00:02     [build-local-dists]
19:09:17 00:02     [requirements]
19:09:17 00:02     [sources]
19:09:18 00:03   [compile]
19:09:18 00:03     [compile-jvm-prep-command]
19:09:18 00:03       [jvm_prep_command]
19:09:18 00:03     [compile-prep-command]
19:09:18 00:03     [compile]
19:09:18 00:03     [rsc]
19:09:18 00:03     [zinc]
19:09:18 00:03     [javac]
19:09:18 00:03   [resources]
19:09:18 00:03     [prepare]
19:09:18 00:03     [services]
19:09:18 00:03   [test]
19:09:18 00:03     [test-jvm-prep-command]
19:09:18 00:03       [jvm_prep_command]
19:09:18 00:03     [test-prep-command]
19:09:18 00:03     [test]
19:09:18 00:03     [pytest-prep]
19:09:18 00:03     [pytest]
19:09:18 00:03       [cache]
                   No cached artifacts for 1 target.
                   Invalidated 1 target.
19:09:18 00:03       [run]
                     Failed to execute PEX file, missing macosx_10_14_x86_64-cp-36-cp36m compatible dependencies for:
                     cffi

                   src/python:test                                                                 .....   NOT RUN
FAILURE


               Waiting for background workers to finish.
19:09:19 00:04   [complete]
               FAILURE
```

To see my locally found dependencies:

```shell
% ls .pants.d/python-setup/resolved_requirements/CPython-3.6.1/cffi*
.pants.d/python-setup/resolved_requirements/CPython-3.6.1/cffi-1.12.3-cp36-cp36m-manylinux1_x86_64.whl
```
