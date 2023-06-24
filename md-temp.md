In this blog post, I will explain why the compiler seemed not to link to libraries despite I write "target_link_libraries(mpp_linux_demo mpp pthread drm)" in CMakeList.txt. This is a common problem that many CMake users face when they try to build their projects with external libraries. The solution is not very complicated, but it requires some understanding of how CMake works and how it handles library dependencies.

The first thing to know is that CMake does not actually link libraries directly. It only generates the commands for the linker to do so. This means that CMake needs to know where to find the libraries and what their names are. This information is usually provided by using find_package() or find_library() commands in CMakeLists.txt. These commands search for the libraries in standard locations or in custom paths specified by the user. They also set some variables that can be used later to refer to the libraries.

For example, if we want to use the mpp library, we can write something like this in CMakeLists.txt:
```
find_package(mpp REQUIRED)
target_link_libraries(mpp_linux_demo ${mpp_LIBRARIES})
```

This will tell CMake to look for the mpp package and set the mpp_LIBRARIES variable with the name of the library (or libraries) that need to be linked. Then, we can use this variable in target_link_libraries() to tell CMake to pass it to the linker.

However, sometimes find_package() or find_library() may not work as expected. They may not find the libraries or they may find the wrong ones. This can happen for various reasons, such as:

- The libraries are installed in non-standard locations and CMake does not know where to look for them.
- The libraries have different names than what CMake expects (e.g., libmpp.so instead of mpp.so).
- The libraries have different versions than what CMake expects (e.g., mpp 2.0 instead of mpp 1.0).
- The libraries have different architectures than what CMake expects (e.g., 32-bit instead of 64-bit).

In these cases, we need to provide more information to CMake about where and how to find the libraries. There are several ways to do this, but one of the most common ones is to use target_include_directories() and target_link_directories() commands. These commands allow us to specify additional paths for CMake to search for headers and libraries, respectively.

For example, if we know that the mpp library is installed in /usr/local/lib/mpp and its header files are in /usr/local/include/mpp, we can write something like this in CMakeLists.txt:
```
target_include_directories(mpp_linux_demo PRIVATE /usr/local/include/mpp)
target_link_directories(mpp_linux_demo PRIVATE /usr/local/lib/mpp)
target_link_libraries(mpp_linux_demo mpp)
```
This will tell CMake to add /usr/local/include/mpp and /usr/local/lib/mpp to the search paths for headers and libraries, respectively. Then, it will tell CMake to link mpp_linux_demo with mpp.

Note that we use PRIVATE keyword here because we only want these paths to be used for this target and not for other targets that may depend on it. If we want these paths to be propagated to other targets, we can use PUBLIC or INTERFACE keywords instead.

Another way to provide more information to CMake about where and how to find the libraries is to use imported targets. Imported targets are special targets that represent external libraries that are not built by CMake. They can be created by using add_library() command with IMPORTED keyword and setting some properties that describe the library.

For example, if we want to create an imported target for the mpp library, we can write something like this in CMakeLists.txt:
```
add_library(mpp SHARED IMPORTED)
set_target_properties(mpp PROPERTIES
  IMPORTED_LOCATION /usr/local/lib/mpp/libmpp.so
  INTERFACE_INCLUDE_DIRECTORIES /usr/local/include/mpp
)
```
This will tell CMake that there is a library called mpp that is imported from /usr/local/lib/mpp/libmpp.so and its header files are in /usr/local/include/mpp. Then, we can use this target in target_link_libraries() as usual:

target_link_libraries(mpp_linux_demo mpp)

This will tell CMake to link mpp_linux_demo with mpp and also add /usr/local/include/mpp to the search path for headers.

Imported targets are useful because they encapsulate all the information about the library in one place and make it easier to reuse them in different projects. They can also be provided by third-party modules or packages that use find_package() or find_library() internally.

To summarize, the reason why the compiler seemed not to link to libraries despite I write "target_link_libraries(mpp_linux_demo mpp pthread drm)" in CMakeList.txt is that CMake did not know where and how to find the libraries. To solve this problem, we need to provide more information to CMake by using target_include_directories(), target_link_directories(), or imported targets. These commands will help CMake to generate the correct commands for the linker and make our project build successfully.