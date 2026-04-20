# As defined by https://learn.microsoft.com/en-us/cpp/intrinsics/arm64-intrinsics?view=msvc-180
MSVC_BUILTINS = {
    # ARM64-specific intrinsics listing
    "arm64": {
        "__break": {"proto": "void __break(int);", "call": "__break(0);"},
        "__addx18byte": {
            "proto": "void __addx18byte(unsigned long, unsigned char);",
            "call": "__addx18byte(0, 0);",
        },
        "__addx18word": {
            "proto": "void __addx18word(unsigned long, unsigned short);",
            "call": "__addx18word(0, 0);",
        },
        "__addx18dword": {
            "proto": "void __addx18dword(unsigned long, unsigned long);",
            "call": "__addx18dword(0, 0);",
        },
        "__addx18qword": {
            "proto": "void __addx18qword(unsigned long, unsigned __int64);",
            "call": "__addx18qword(0, 0);",
        },
        "__cas8": {
            "proto": "unsigned __int8 __cas8(unsigned __int8 volatile*, unsigned __int8, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __cas8(&tgt, 0, 0);",
        },
        "__cas16": {
            "proto": "unsigned __int16 __cas16(unsigned __int16 volatile*, unsigned __int16, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __cas16(&tgt, 0, 0);",
        },
        "__cas32": {
            "proto": "unsigned __int32 __cas32(unsigned __int32 volatile*, unsigned __int32, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __cas32(&tgt, 0, 0);",
        },
        "__cas64": {
            "proto": "unsigned __int64 __cas64(unsigned __int64 volatile*, unsigned __int64, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __cas64(&tgt, 0, 0);",
        },
        "__casa8": {
            "proto": "unsigned __int8 __casa8(unsigned __int8 volatile*, unsigned __int8, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __casa8(&tgt, 0, 0);",
        },
        "__casa16": {
            "proto": "unsigned __int16 __casa16(unsigned __int16 volatile*, unsigned __int16, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __casa16(&tgt, 0, 0);",
        },
        "__casa32": {
            "proto": "unsigned __int32 __casa32(unsigned __int32 volatile*, unsigned __int32, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __casa32(&tgt, 0, 0);",
        },
        "__casa64": {
            "proto": "unsigned __int64 __casa64(unsigned __int64 volatile*, unsigned __int64, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __casa64(&tgt, 0, 0);",
        },
        "__casl8": {
            "proto": "unsigned __int8 __casl8(unsigned __int8 volatile*, unsigned __int8, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __casl8(&tgt, 0, 0);",
        },
        "__casl16": {
            "proto": "unsigned __int16 __casl16(unsigned __int16 volatile*, unsigned __int16, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __casl16(&tgt, 0, 0);",
        },
        "__casl32": {
            "proto": "unsigned __int32 __casl32(unsigned __int32 volatile*, unsigned __int32, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __casl32(&tgt, 0, 0);",
        },
        "__casl64": {
            "proto": "unsigned __int64 __casl64(unsigned __int64 volatile*, unsigned __int64, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __casl64(&tgt, 0, 0);",
        },
        "__casal8": {
            "proto": "unsigned __int8 __casal8(unsigned __int8 volatile*, unsigned __int8, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __casal8(&tgt, 0, 0);",
        },
        "__casal16": {
            "proto": "unsigned __int16 __casal16(unsigned __int16 volatile*, unsigned __int16, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __casal16(&tgt, 0, 0);",
        },
        "__casal32": {
            "proto": "unsigned __int32 __casal32(unsigned __int32 volatile*, unsigned __int32, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __casal32(&tgt, 0, 0);",
        },
        "__casal64": {
            "proto": "unsigned __int64 __casal64(unsigned __int64 volatile*, unsigned __int64, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __casal64(&tgt, 0, 0);",
        },
        "__crc32b": {
            "proto": "unsigned __int32 __crc32b(unsigned __int32, unsigned __int32);",
            "call": "__crc32b(0, 0);",
            "arch": "+crc",
        },
        "__crc32h": {
            "proto": "unsigned __int32 __crc32h(unsigned __int32, unsigned __int32);",
            "call": "__crc32h(0, 0);",
            "arch": "+crc",
        },
        "__crc32w": {
            "proto": "unsigned __int32 __crc32w(unsigned __int32, unsigned __int32);",
            "call": "__crc32w(0, 0);",
            "arch": "+crc",
        },
        "__crc32d": {
            "proto": "unsigned __int32 __crc32d(unsigned __int32, unsigned __int64);",
            "call": "__crc32d(0, 0);",
            "arch": "+crc",
        },
        "__crc32cb": {
            "proto": "unsigned __int32 __crc32cb(unsigned __int32, unsigned __int32);",
            "call": "__crc32cb(0, 0);",
            "arch": "+crc",
        },
        "__crc32ch": {
            "proto": "unsigned __int32 __crc32ch(unsigned __int32, unsigned __int32);",
            "call": "__crc32ch(0, 0);",
            "arch": "+crc",
        },
        "__crc32cw": {
            "proto": "unsigned __int32 __crc32cw(unsigned __int32, unsigned __int32);",
            "call": "__crc32cw(0, 0);",
            "arch": "+crc",
        },
        "__crc32cd": {
            "proto": "unsigned __int32 __crc32cd(unsigned __int32, unsigned __int64);",
            "call": "__crc32cd(0, 0);",
            "arch": "+crc",
        },
        "__dmb": {"proto": "void __dmb(unsigned int);", "call": "__dmb(0);"},
        "__dsb": {"proto": "void __dsb(unsigned int);", "call": "__dsb(0);"},
        "__isb": {"proto": "void __isb(unsigned int);", "call": "__isb(0);"},
        "__getReg": {
            "proto": "unsigned __int64 __getReg(int);",
            "call": "__getReg(0);",
        },
        "__getRegFp": {"proto": "double __getRegFp(int);", "call": "__getRegFp(0);"},
        # __getCallerReg only works with non-volatile (callee-saved) registers
        # or dedicated architectural registers.
        "__getCallerReg": {
            "proto": "unsigned __int64 __getCallerReg(int);",
            "call": "__getCallerReg(30);",
        },
        # __getCallerRegFp only works with non-volatile (callee-saved) registers.
        "__getCallerRegFp": {
            "proto": "double __getCallerRegFp(int);",
            "call": "__getCallerRegFp(8);",
        },
        "__hvc": {
            "proto": "unsigned int __hvc(unsigned int, ...);",
            "call": "__hvc(0);",
        },
        "__hlt": {"proto": "int __hlt(unsigned int, ...);", "call": "__hlt(0);"},
        "__incx18byte": {
            "proto": "void __incx18byte(unsigned long);",
            "call": "__incx18byte(0);",
        },
        "__incx18word": {
            "proto": "void __incx18word(unsigned long);",
            "call": "__incx18word(0);",
        },
        "__incx18dword": {
            "proto": "void __incx18dword(unsigned long);",
            "call": "__incx18dword(0);",
        },
        "__incx18qword": {
            "proto": "void __incx18qword(unsigned long);",
            "call": "__incx18qword(0);",
        },
        "__iso_volatile_load8": {
            "proto": "__int8 __iso_volatile_load8(const volatile __int8 *);",
            "call": "__int8 tgt = 0; __iso_volatile_load8(&tgt);",
        },
        "__iso_volatile_load16": {
            "proto": "__int16 __iso_volatile_load16(const volatile __int16 *);",
            "call": "__int16 tgt = 0; __iso_volatile_load16(&tgt);",
        },
        "__iso_volatile_load32": {
            "proto": "__int32 __iso_volatile_load32(const volatile __int32 *);",
            "call": "__int32 tgt = 0; __iso_volatile_load32(&tgt);",
        },
        "__iso_volatile_load64": {
            "proto": "__int64 __iso_volatile_load64(const volatile __int64 *);",
            "call": "__int64 tgt = 0; __iso_volatile_load64(&tgt);",
        },
        "__iso_volatile_store8": {
            "proto": "void __iso_volatile_store8(volatile __int8 *, __int8);",
            "call": "__int8 tgt = 0; __iso_volatile_store8(&tgt, 0);",
        },
        "__iso_volatile_store16": {
            "proto": "void __iso_volatile_store16(volatile __int16 *, __int16);",
            "call": "__int16 tgt = 0; __iso_volatile_store16(&tgt, 0);",
        },
        "__iso_volatile_store32": {
            "proto": "void __iso_volatile_store32(volatile __int32 *, __int32);",
            "call": "__int32 tgt = 0; __iso_volatile_store32(&tgt, 0);",
        },
        "__iso_volatile_store64": {
            "proto": "void __iso_volatile_store64(volatile __int64 *, __int64);",
            "call": "__int64 tgt = 0; __iso_volatile_store64(&tgt, 0);",
        },
        "__ldar8": {
            "proto": "unsigned __int8 __ldar8(const unsigned __int8 volatile*);",
            "call": "unsigned __int8 tgt = 0; __ldar8(&tgt);",
        },
        "__ldar16": {
            "proto": "unsigned __int16 __ldar16(const unsigned __int16 volatile*);",
            "call": "unsigned __int16 tgt = 0; __ldar16(&tgt);",
        },
        "__ldar32": {
            "proto": "unsigned __int32 __ldar32(const unsigned __int32 volatile*);",
            "call": "unsigned __int32 tgt = 0; __ldar32(&tgt);",
        },
        "__ldar64": {
            "proto": "unsigned __int64 __ldar64(const unsigned __int64 volatile*);",
            "call": "unsigned __int64 tgt = 0; __ldar64(&tgt);",
        },
        "__ldapr8": {
            "proto": "unsigned __int8 __ldapr8(unsigned __int8 volatile*);",
            "call": "unsigned __int8 tgt = 0; __ldapr8(&tgt);",
        },
        "__ldapr16": {
            "proto": "unsigned __int16 __ldapr16(unsigned __int16 volatile*);",
            "call": "unsigned __int16 tgt = 0; __ldapr16(&tgt);",
        },
        "__ldapr32": {
            "proto": "unsigned __int32 __ldapr32(unsigned __int32 volatile*);",
            "call": "unsigned __int32 tgt = 0; __ldapr32(&tgt);",
        },
        "__ldapr64": {
            "proto": "unsigned __int64 __ldapr64(unsigned __int64 volatile*);",
            "call": "unsigned __int64 tgt = 0; __ldapr64(&tgt);",
        },
        "__mulh": {
            "proto": "__int64 __mulh(__int64, __int64);",
            "call": "__mulh(0, 0);",
        },
        "__umulh": {
            "proto": "unsigned __int64 __umulh(unsigned __int64, unsigned __int64);",
            "call": "__umulh(0, 0);",
        },
        "__prefetch": {
            "proto": "void __cdecl __prefetch(const void *);",
            "call": "int dummy = 0; __prefetch(&dummy);",
        },
        "__prefetch2": {
            "proto": "void __cdecl __prefetch2(const void *, uint8_t);",
            "call": "int dummy = 0; __prefetch2(&dummy, 0);",
        },
        "__readx18byte": {
            "proto": "unsigned char __readx18byte(unsigned long);",
            "call": "__readx18byte(0);",
        },
        "__readx18word": {
            "proto": "unsigned short __readx18word(unsigned long);",
            "call": "__readx18word(0);",
        },
        "__readx18dword": {
            "proto": "unsigned long __readx18dword(unsigned long);",
            "call": "__readx18dword(0);",
        },
        "__readx18qword": {
            "proto": "unsigned __int64 __readx18qword(unsigned long);",
            "call": "__readx18qword(0);",
        },
        "__writex18byte": {
            "proto": "void __writex18byte(unsigned long, unsigned char);",
            "call": "__writex18byte(0, 0);",
        },
        "__writex18word": {
            "proto": "void __writex18word(unsigned long, unsigned short);",
            "call": "__writex18word(0, 0);",
        },
        "__writex18dword": {
            "proto": "void __writex18dword(unsigned long, unsigned long);",
            "call": "__writex18dword(0, 0);",
        },
        "__writex18qword": {
            "proto": "void __writex18qword(unsigned long, unsigned __int64);",
            "call": "__writex18qword(0, 0);",
        },
        "__setReg": {
            "proto": "void __setReg(int, unsigned __int64);",
            "call": "__setReg(0, 0);",
        },
        "__setRegFp": {
            "proto": "void __setRegFp(int, double);",
            "call": "__setRegFp(0, 0.0);",
        },
        "__setCallerReg": {
            "proto": "void __setCallerReg(int, unsigned __int64);",
            "call": "__setCallerReg(19, 0);",
        },
        "__setCallerRegFp": {
            "proto": "void __setCallerRegFp(int, double);",
            "call": "__setCallerRegFp(8, 0.0);",
        },
        "__sev": {"proto": "void __sev(void);", "call": "__sev();"},
        "__wfe": {"proto": "void __wfe(void);", "call": "__wfe();"},
        "__wfi": {"proto": "void __wfi(void);", "call": "__wfi();"},
        "__svc": {
            "proto": "unsigned int __svc(unsigned int, ...);",
            "call": "__svc(0);",
        },
        "__sys": {"proto": "unsigned int __sys(int, __int64);", "call": "__sys(0, 0);"},
        "__static_assert": {
            "proto": "void __static_assert(int, const char *);",
            "call": '__static_assert(1, "test");',
        },
        "__stlr8": {
            "proto": "void __stlr8(unsigned __int8 volatile*, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __stlr8(&tgt, 0);",
        },
        "__stlr16": {
            "proto": "void __stlr16(unsigned __int16 volatile*, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __stlr16(&tgt, 0);",
        },
        "__stlr32": {
            "proto": "void __stlr32(unsigned __int32 volatile*, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __stlr32(&tgt, 0);",
        },
        "__stlr64": {
            "proto": "void __stlr64(unsigned __int64 volatile*, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __stlr64(&tgt, 0);",
        },
        "__swp8": {
            "proto": "unsigned __int8 __swp8(unsigned __int8 volatile*, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __swp8(&tgt, 0);",
        },
        "__swp16": {
            "proto": "unsigned __int16 __swp16(unsigned __int16 volatile*, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __swp16(&tgt, 0);",
        },
        "__swp32": {
            "proto": "unsigned __int32 __swp32(unsigned __int32 volatile*, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __swp32(&tgt, 0);",
        },
        "__swp64": {
            "proto": "unsigned __int64 __swp64(unsigned __int64 volatile*, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __swp64(&tgt, 0);",
        },
        "__swpa8": {
            "proto": "unsigned __int8 __swpa8(unsigned __int8 volatile*, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __swpa8(&tgt, 0);",
        },
        "__swpa16": {
            "proto": "unsigned __int16 __swpa16(unsigned __int16 volatile*, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __swpa16(&tgt, 0);",
        },
        "__swpa32": {
            "proto": "unsigned __int32 __swpa32(unsigned __int32 volatile*, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __swpa32(&tgt, 0);",
        },
        "__swpa64": {
            "proto": "unsigned __int64 __swpa64(unsigned __int64 volatile*, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __swpa64(&tgt, 0);",
        },
        "__swpl8": {
            "proto": "unsigned __int8 __swpl8(unsigned __int8 volatile*, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __swpl8(&tgt, 0);",
        },
        "__swpl16": {
            "proto": "unsigned __int16 __swpl16(unsigned __int16 volatile*, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __swpl16(&tgt, 0);",
        },
        "__swpl32": {
            "proto": "unsigned __int32 __swpl32(unsigned __int32 volatile*, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __swpl32(&tgt, 0);",
        },
        "__swpl64": {
            "proto": "unsigned __int64 __swpl64(unsigned __int64 volatile*, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __swpl64(&tgt, 0);",
        },
        "__swpal8": {
            "proto": "unsigned __int8 __swpal8(unsigned __int8 volatile*, unsigned __int8);",
            "call": "unsigned __int8 tgt = 0; __swpal8(&tgt, 0);",
        },
        "__swpal16": {
            "proto": "unsigned __int16 __swpal16(unsigned __int16 volatile*, unsigned __int16);",
            "call": "unsigned __int16 tgt = 0; __swpal16(&tgt, 0);",
        },
        "__swpal32": {
            "proto": "unsigned __int32 __swpal32(unsigned __int32 volatile*, unsigned __int32);",
            "call": "unsigned __int32 tgt = 0; __swpal32(&tgt, 0);",
        },
        "__swpal64": {
            "proto": "unsigned __int64 __swpal64(unsigned __int64 volatile*, unsigned __int64);",
            "call": "unsigned __int64 tgt = 0; __swpal64(&tgt, 0);",
        },
        "_CopyDoubleFromInt64": {
            "proto": "double _CopyDoubleFromInt64(__int64);",
            "call": "_CopyDoubleFromInt64(0);",
        },
        "_CopyFloatFromInt32": {
            "proto": "float _CopyFloatFromInt32(__int32);",
            "call": "_CopyFloatFromInt32(0);",
        },
        "_CopyInt32FromFloat": {
            "proto": "__int32 _CopyInt32FromFloat(float);",
            "call": "_CopyInt32FromFloat(0.0f);",
        },
        "_CopyInt64FromDouble": {
            "proto": "__int64 _CopyInt64FromDouble(double);",
            "call": "_CopyInt64FromDouble(0.0);",
        },
        "_CountLeadingOnes": {
            "proto": "unsigned int _CountLeadingOnes(unsigned long);",
            "call": "_CountLeadingOnes(0);",
        },
        "_CountLeadingOnes64": {
            "proto": "unsigned int _CountLeadingOnes64(unsigned __int64);",
            "call": "_CountLeadingOnes64(0);",
        },
        "_CountLeadingSigns": {
            "proto": "unsigned int _CountLeadingSigns(long);",
            "call": "_CountLeadingSigns(0);",
        },
        "_CountLeadingSigns64": {
            "proto": "unsigned int _CountLeadingSigns64(__int64);",
            "call": "_CountLeadingSigns64(0);",
        },
        "_CountLeadingZeros": {
            "proto": "unsigned int _CountLeadingZeros(unsigned long);",
            "call": "_CountLeadingZeros(0);",
        },
        "_CountLeadingZeros64": {
            "proto": "unsigned int _CountLeadingZeros64(unsigned __int64);",
            "call": "_CountLeadingZeros64(0);",
        },
        "_CountTrailingZeros": {
            "proto": "unsigned int _CountTrailingZeros(unsigned long);",
            "call": "_CountTrailingZeros(0);",
        },
        "_CountTrailingZeros64": {
            "proto": "unsigned int _CountTrailingZeros64(unsigned __int64);",
            "call": "_CountTrailingZeros64(0);",
        },
        "_CountOneBits": {
            "proto": "unsigned int _CountOneBits(unsigned long);",
            "call": "_CountOneBits(0);",
        },
        "_CountOneBits64": {
            "proto": "unsigned int _CountOneBits64(unsigned __int64);",
            "call": "_CountOneBits64(0);",
        },
        "_ReadStatusReg": {
            "proto": "__int64 _ReadStatusReg(int);",
            "call": "_ReadStatusReg(16384);",
        },
        "_WriteStatusReg": {
            "proto": "void _WriteStatusReg(int, __int64);",
            "call": "_WriteStatusReg(16384, 0);",
        },
    },
    # __iso_volatile_load/store intrinsics
    "iso_load_store": {
        "__iso_volatile_load8": {
            "proto": "__int8 __iso_volatile_load8(const volatile __int8 * Location);",
            "call": "__int8 tgt = 0; __iso_volatile_load8(&tgt);",
        },
        "__iso_volatile_load16": {
            "proto": "__int16 __iso_volatile_load16(const volatile __int16 * Location);",
            "call": "__int16 tgt = 0; __iso_volatile_load16(&tgt);",
        },
        "__iso_volatile_load32": {
            "proto": "__int32 __iso_volatile_load32(const volatile __int32 * Location);",
            "call": "__int32 tgt = 0; __iso_volatile_load32(&tgt);",
        },
        "__iso_volatile_load64": {
            "proto": "__int64 __iso_volatile_load64(const volatile __int64 * Location);",
            "call": "__int64 tgt = 0; __iso_volatile_load64(&tgt);",
        },
        "__iso_volatile_store8": {
            "proto": "void __iso_volatile_store8(volatile __int8 * Location, __int8 Value);",
            "call": "__int8 tgt = 0; __iso_volatile_store8(&tgt, 0);",
        },
        "__iso_volatile_store16": {
            "proto": "void __iso_volatile_store16(volatile __int16 * Location, __int16 Value);",
            "call": "__int16 tgt = 0; __iso_volatile_store16(&tgt, 0);",
        },
        "__iso_volatile_store32": {
            "proto": "void __iso_volatile_store32(volatile __int32 * Location, __int32 Value);",
            "call": "__int32 tgt = 0; __iso_volatile_store32(&tgt, 0);",
        },
        "__iso_volatile_store64": {
            "proto": "void __iso_volatile_store64(volatile __int64 * Location, __int64 Value);",
            "call": "__int64 tgt = 0; __iso_volatile_store64(&tgt, 0);",
        },
    },
    # ARM64 support for intrinsics from other architectures
    "general": {
        "__assume": {"proto": "void __assume(int);", "call": "__assume(1);"},
        "__code_seg": {
            "proto": "void __code_seg(const char *);",
            "call": '__code_seg("text");',
        },
        "__debugbreak": {
            "proto": "void __cdecl __debugbreak(void);",
            "call": "__debugbreak();",
        },
        "__fastfail": {
            "proto": "__declspec(noreturn) void __fastfail(unsigned int);",
            "call": "__fastfail(0);",
        },
        "__nop": {"proto": "void __nop(void);", "call": "__nop();"},
        "__yield": {"proto": "void __yield(void);", "call": "__yield();"},
        "_AddressOfReturnAddress": {
            "proto": "void * _AddressOfReturnAddress(void);",
            "call": "void* ptr = _AddressOfReturnAddress();",
        },
        "_BitScanForward": {
            "proto": "unsigned char _BitScanForward(unsigned long * _Index, unsigned long _Mask);",
            "call": "unsigned long idx = 0; _BitScanForward(&idx, 1);",
        },
        "_BitScanForward64": {
            "proto": "unsigned char _BitScanForward64(unsigned long * _Index, unsigned __int64 _Mask);",
            "call": "unsigned long idx = 0; _BitScanForward64(&idx, 1);",
        },
        "_BitScanReverse": {
            "proto": "unsigned char _BitScanReverse(unsigned long * _Index, unsigned long _Mask);",
            "call": "unsigned long idx = 0; _BitScanReverse(&idx, 1);",
        },
        "_BitScanReverse64": {
            "proto": "unsigned char _BitScanReverse64(unsigned long * _Index, unsigned __int64 _Mask);",
            "call": "unsigned long idx = 0; _BitScanReverse64(&idx, 1);",
        },
        "_bittest": {
            "proto": "unsigned char _bittest(long const *, long);",
            "call": "long val = 0; _bittest(&val, 0);",
        },
        "_bittest64": {
            "proto": "unsigned char _bittest64(__int64 const *, __int64);",
            "call": "__int64 val = 0; _bittest64(&val, 0);",
        },
        "_bittestandcomplement": {
            "proto": "unsigned char _bittestandcomplement(long *, long);",
            "call": "long val = 0; _bittestandcomplement(&val, 0);",
        },
        "_bittestandcomplement64": {
            "proto": "unsigned char _bittestandcomplement64(__int64 *, __int64);",
            "call": "__int64 val = 0; _bittestandcomplement64(&val, 0);",
        },
        "_bittestandreset": {
            "proto": "unsigned char _bittestandreset(long *, long);",
            "call": "long val = 0; _bittestandreset(&val, 0);",
        },
        "_bittestandreset64": {
            "proto": "unsigned char _bittestandreset64(__int64 *, __int64);",
            "call": "__int64 val = 0; _bittestandreset64(&val, 0);",
        },
        "_bittestandset": {
            "proto": "unsigned char _bittestandset(long *, long);",
            "call": "long val = 0; _bittestandset(&val, 0);",
        },
        "_bittestandset64": {
            "proto": "unsigned char _bittestandset64(__int64 *, __int64);",
            "call": "__int64 val = 0; _bittestandset64(&val, 0);",
        },
        "_byteswap_uint64": {
            "proto": "unsigned __int64 __cdecl _byteswap_uint64(unsigned __int64);",
            "call": "_byteswap_uint64(0);",
        },
        "_byteswap_ulong": {
            "proto": "unsigned long __cdecl _byteswap_ulong(unsigned long);",
            "call": "_byteswap_ulong(0);",
        },
        "_byteswap_ushort": {
            "proto": "unsigned short __cdecl _byteswap_ushort(unsigned short);",
            "call": "_byteswap_ushort(0);",
        },
        "_disable": {"proto": "void __cdecl _disable(void);", "call": "_disable();"},
        "_enable": {"proto": "void __cdecl _enable(void);", "call": "_enable();"},
        "_lrotl": {
            "proto": "unsigned long __cdecl _lrotl(unsigned long, int);",
            "call": "_lrotl(0, 0);",
        },
        "_lrotr": {
            "proto": "unsigned long __cdecl _lrotr(unsigned long, int);",
            "call": "_lrotr(0, 0);",
        },
        "_ReadBarrier": {
            "proto": "void _ReadBarrier(void);",
            "call": "_ReadBarrier();",
        },
        "_ReadWriteBarrier": {
            "proto": "void _ReadWriteBarrier(void);",
            "call": "_ReadWriteBarrier();",
        },
        "_ReturnAddress": {
            "proto": "void * _ReturnAddress(void);",
            "call": "void* ptr = _ReturnAddress();",
        },
        "_rotl": {
            "proto": "unsigned int __cdecl _rotl(unsigned int _Value, int _Shift);",
            "call": "_rotl(0, 0);",
        },
        "_rotl16": {
            "proto": "unsigned short _rotl16(unsigned short _Value, unsigned char _Shift);",
            "call": "_rotl16(0, 0);",
        },
        "_rotl64": {
            "proto": "unsigned __int64 __cdecl _rotl64(unsigned __int64 _Value, int _Shift);",
            "call": "_rotl64(0, 0);",
        },
        "_rotl8": {
            "proto": "unsigned char _rotl8(unsigned char _Value, unsigned char _Shift);",
            "call": "_rotl8(0, 0);",
        },
        "_rotr": {
            "proto": "unsigned int __cdecl _rotr(unsigned int _Value, int _Shift);",
            "call": "_rotr(0, 0);",
        },
        "_rotr16": {
            "proto": "unsigned short _rotr16(unsigned short _Value, unsigned char _Shift);",
            "call": "_rotr16(0, 0);",
        },
        "_rotr64": {
            "proto": "unsigned __int64 __cdecl _rotr64(unsigned __int64 _Value, int _Shift);",
            "call": "_rotr64(0, 0);",
        },
        "_rotr8": {
            "proto": "unsigned char _rotr8(unsigned char _Value, unsigned char _Shift);",
            "call": "_rotr8(0, 0);",
        },
        "_setjmpex": {
            "proto": "int __cdecl _setjmpex(jmp_buf);",
            "call": "jmp_buf buf; _setjmpex(buf);",
        },
        "_WriteBarrier": {
            "proto": "void _WriteBarrier(void);",
            "call": "_WriteBarrier();",
        },
    },
    # 4. Atomic Interlocked builtins list
    "interlocked": {
        # Add (long)
        "_InterlockedAdd": {
            "proto": "long _InterlockedAdd(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAdd(&tgt, 0);",
        },
        "_InterlockedAdd_acq": {
            "proto": "long _InterlockedAdd_acq(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAdd_acq(&tgt, 0);",
        },
        "_InterlockedAdd_nf": {
            "proto": "long _InterlockedAdd_nf(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAdd_nf(&tgt, 0);",
        },
        "_InterlockedAdd_rel": {
            "proto": "long _InterlockedAdd_rel(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAdd_rel(&tgt, 0);",
        },
        # Add (64)
        "_InterlockedAdd64": {
            "proto": "__int64 _InterlockedAdd64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAdd64(&tgt, 0);",
        },
        "_InterlockedAdd64_acq": {
            "proto": "__int64 _InterlockedAdd64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAdd64_acq(&tgt, 0);",
        },
        "_InterlockedAdd64_nf": {
            "proto": "__int64 _InterlockedAdd64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAdd64_nf(&tgt, 0);",
        },
        "_InterlockedAdd64_rel": {
            "proto": "__int64 _InterlockedAdd64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAdd64_rel(&tgt, 0);",
        },
        # And (long)
        "_InterlockedAnd": {
            "proto": "long _InterlockedAnd(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAnd(&tgt, 0);",
        },
        "_InterlockedAnd_acq": {
            "proto": "long _InterlockedAnd_acq(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAnd_acq(&tgt, 0);",
        },
        "_InterlockedAnd_nf": {
            "proto": "long _InterlockedAnd_nf(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAnd_nf(&tgt, 0);",
        },
        "_InterlockedAnd_rel": {
            "proto": "long _InterlockedAnd_rel(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedAnd_rel(&tgt, 0);",
        },
        # And (8)
        "_InterlockedAnd8": {
            "proto": "char _InterlockedAnd8(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedAnd8(&tgt, 0);",
        },
        "_InterlockedAnd8_acq": {
            "proto": "char _InterlockedAnd8_acq(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedAnd8_acq(&tgt, 0);",
        },
        "_InterlockedAnd8_nf": {
            "proto": "char _InterlockedAnd8_nf(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedAnd8_nf(&tgt, 0);",
        },
        "_InterlockedAnd8_rel": {
            "proto": "char _InterlockedAnd8_rel(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedAnd8_rel(&tgt, 0);",
        },
        # And (16)
        "_InterlockedAnd16": {
            "proto": "short _InterlockedAnd16(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedAnd16(&tgt, 0);",
        },
        "_InterlockedAnd16_acq": {
            "proto": "short _InterlockedAnd16_acq(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedAnd16_acq(&tgt, 0);",
        },
        "_InterlockedAnd16_nf": {
            "proto": "short _InterlockedAnd16_nf(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedAnd16_nf(&tgt, 0);",
        },
        "_InterlockedAnd16_rel": {
            "proto": "short _InterlockedAnd16_rel(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedAnd16_rel(&tgt, 0);",
        },
        # And (64)
        "_InterlockedAnd64": {
            "proto": "__int64 _InterlockedAnd64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAnd64(&tgt, 0);",
        },
        "_InterlockedAnd64_acq": {
            "proto": "__int64 _InterlockedAnd64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAnd64_acq(&tgt, 0);",
        },
        "_InterlockedAnd64_nf": {
            "proto": "__int64 _InterlockedAnd64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAnd64_nf(&tgt, 0);",
        },
        "_InterlockedAnd64_rel": {
            "proto": "__int64 _InterlockedAnd64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedAnd64_rel(&tgt, 0);",
        },
        # CompareExchange (long)
        "_InterlockedCompareExchange": {
            "proto": "long __cdecl _InterlockedCompareExchange(long volatile *, long, long);",
            "call": "long tgt = 0; _InterlockedCompareExchange(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange_acq": {
            "proto": "long _InterlockedCompareExchange_acq(long volatile *, long, long);",
            "call": "long tgt = 0; _InterlockedCompareExchange_acq(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange_nf": {
            "proto": "long _InterlockedCompareExchange_nf(long volatile *, long, long);",
            "call": "long tgt = 0; _InterlockedCompareExchange_nf(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange_rel": {
            "proto": "long _InterlockedCompareExchange_rel(long volatile *, long, long);",
            "call": "long tgt = 0; _InterlockedCompareExchange_rel(&tgt, 0, 0);",
        },
        # CompareExchange (8)
        "_InterlockedCompareExchange8": {
            "proto": "char _InterlockedCompareExchange8(char volatile *, char, char);",
            "call": "char tgt = 0; _InterlockedCompareExchange8(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange8_acq": {
            "proto": "char _InterlockedCompareExchange8_acq(char volatile *, char, char);",
            "call": "char tgt = 0; _InterlockedCompareExchange8_acq(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange8_nf": {
            "proto": "char _InterlockedCompareExchange8_nf(char volatile *, char, char);",
            "call": "char tgt = 0; _InterlockedCompareExchange8_nf(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange8_rel": {
            "proto": "char _InterlockedCompareExchange8_rel(char volatile *, char, char);",
            "call": "char tgt = 0; _InterlockedCompareExchange8_rel(&tgt, 0, 0);",
        },
        # CompareExchange (16)
        "_InterlockedCompareExchange16": {
            "proto": "short _InterlockedCompareExchange16(short volatile *, short, short);",
            "call": "short tgt = 0; _InterlockedCompareExchange16(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange16_acq": {
            "proto": "short _InterlockedCompareExchange16_acq(short volatile *, short, short);",
            "call": "short tgt = 0; _InterlockedCompareExchange16_acq(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange16_nf": {
            "proto": "short _InterlockedCompareExchange16_nf(short volatile *, short, short);",
            "call": "short tgt = 0; _InterlockedCompareExchange16_nf(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange16_rel": {
            "proto": "short _InterlockedCompareExchange16_rel(short volatile *, short, short);",
            "call": "short tgt = 0; _InterlockedCompareExchange16_rel(&tgt, 0, 0);",
        },
        # CompareExchange (64)
        "_InterlockedCompareExchange64": {
            "proto": "__int64 _InterlockedCompareExchange64(__int64 volatile *, __int64, __int64);",
            "call": "__int64 tgt = 0; _InterlockedCompareExchange64(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange64_acq": {
            "proto": "__int64 _InterlockedCompareExchange64_acq(__int64 volatile *, __int64, __int64);",
            "call": "__int64 tgt = 0; _InterlockedCompareExchange64_acq(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange64_nf": {
            "proto": "__int64 _InterlockedCompareExchange64_nf(__int64 volatile *, __int64, __int64);",
            "call": "__int64 tgt = 0; _InterlockedCompareExchange64_nf(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchange64_rel": {
            "proto": "__int64 _InterlockedCompareExchange64_rel(__int64 volatile *, __int64, __int64);",
            "call": "__int64 tgt = 0; _InterlockedCompareExchange64_rel(&tgt, 0, 0);",
        },
        # CompareExchangePointer
        "_InterlockedCompareExchangePointer": {
            "proto": "void * _InterlockedCompareExchangePointer(void * volatile *, void *, void *);",
            "call": "void* tgt = 0; _InterlockedCompareExchangePointer(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchangePointer_acq": {
            "proto": "void * _InterlockedCompareExchangePointer_acq(void * volatile *, void *, void *);",
            "call": "void* tgt = 0; _InterlockedCompareExchangePointer_acq(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchangePointer_nf": {
            "proto": "void * _InterlockedCompareExchangePointer_nf(void * volatile *, void *, void *);",
            "call": "void* tgt = 0; _InterlockedCompareExchangePointer_nf(&tgt, 0, 0);",
        },
        "_InterlockedCompareExchangePointer_rel": {
            "proto": "void * _InterlockedCompareExchangePointer_rel(void * volatile *, void *, void *);",
            "call": "void* tgt = 0; _InterlockedCompareExchangePointer_rel(&tgt, 0, 0);",
        },
        # CompareExchange128
        "_InterlockedCompareExchange128": {
            "proto": "unsigned char _InterlockedCompareExchange128(__int64 volatile * _Destination, __int64 _ExchangeHigh, __int64 _ExchangeLow, __int64 * _ComparandResult);",
            "call": "__int64 tgt = 0; __int64 cmp = 0; _InterlockedCompareExchange128(&tgt, 0, 0, &cmp);",
        },
        "_InterlockedCompareExchange128_acq": {
            "proto": "unsigned char _InterlockedCompareExchange128_acq(__int64 volatile * _Destination, __int64 _ExchangeHigh, __int64 _ExchangeLow, __int64 * _ComparandResult);",
            "call": "__int64 tgt = 0; __int64 cmp = 0; _InterlockedCompareExchange128_acq(&tgt, 0, 0, &cmp);",
        },
        "_InterlockedCompareExchange128_nf": {
            "proto": "unsigned char _InterlockedCompareExchange128_nf(__int64 volatile * _Destination, __int64 _ExchangeHigh, __int64 _ExchangeLow, __int64 * _ComparandResult);",
            "call": "__int64 tgt = 0; __int64 cmp = 0; _InterlockedCompareExchange128_nf(&tgt, 0, 0, &cmp);",
        },
        "_InterlockedCompareExchange128_rel": {
            "proto": "unsigned char _InterlockedCompareExchange128_rel(__int64 volatile * _Destination, __int64 _ExchangeHigh, __int64 _ExchangeLow, __int64 * _ComparandResult);",
            "call": "__int64 tgt = 0; __int64 cmp = 0; _InterlockedCompareExchange128_rel(&tgt, 0, 0, &cmp);",
        },
        # Decrement (long)
        "_InterlockedDecrement": {
            "proto": "long __cdecl _InterlockedDecrement(long volatile *);",
            "call": "long tgt = 0; _InterlockedDecrement(&tgt);",
        },
        "_InterlockedDecrement_acq": {
            "proto": "long _InterlockedDecrement_acq(long volatile *);",
            "call": "long tgt = 0; _InterlockedDecrement_acq(&tgt);",
        },
        "_InterlockedDecrement_nf": {
            "proto": "long _InterlockedDecrement_nf(long volatile *);",
            "call": "long tgt = 0; _InterlockedDecrement_nf(&tgt);",
        },
        "_InterlockedDecrement_rel": {
            "proto": "long _InterlockedDecrement_rel(long volatile *);",
            "call": "long tgt = 0; _InterlockedDecrement_rel(&tgt);",
        },
        # Decrement (16)
        "_InterlockedDecrement16": {
            "proto": "short _InterlockedDecrement16(short volatile *);",
            "call": "short tgt = 0; _InterlockedDecrement16(&tgt);",
        },
        "_InterlockedDecrement16_acq": {
            "proto": "short _InterlockedDecrement16_acq(short volatile *);",
            "call": "short tgt = 0; _InterlockedDecrement16_acq(&tgt);",
        },
        "_InterlockedDecrement16_nf": {
            "proto": "short _InterlockedDecrement16_nf(short volatile *);",
            "call": "short tgt = 0; _InterlockedDecrement16_nf(&tgt);",
        },
        "_InterlockedDecrement16_rel": {
            "proto": "short _InterlockedDecrement16_rel(short volatile *);",
            "call": "short tgt = 0; _InterlockedDecrement16_rel(&tgt);",
        },
        # Decrement (64)
        "_InterlockedDecrement64": {
            "proto": "__int64 _InterlockedDecrement64(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedDecrement64(&tgt);",
        },
        "_InterlockedDecrement64_acq": {
            "proto": "__int64 _InterlockedDecrement64_acq(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedDecrement64_acq(&tgt);",
        },
        "_InterlockedDecrement64_nf": {
            "proto": "__int64 _InterlockedDecrement64_nf(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedDecrement64_nf(&tgt);",
        },
        "_InterlockedDecrement64_rel": {
            "proto": "__int64 _InterlockedDecrement64_rel(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedDecrement64_rel(&tgt);",
        },
        # Exchange (long)
        "_InterlockedExchange": {
            "proto": "long __cdecl _InterlockedExchange(long volatile * _Target, long);",
            "call": "long tgt = 0; _InterlockedExchange(&tgt, 0);",
        },
        "_InterlockedExchange_acq": {
            "proto": "long _InterlockedExchange_acq(long volatile * _Target, long);",
            "call": "long tgt = 0; _InterlockedExchange_acq(&tgt, 0);",
        },
        "_InterlockedExchange_nf": {
            "proto": "long _InterlockedExchange_nf(long volatile * _Target, long);",
            "call": "long tgt = 0; _InterlockedExchange_nf(&tgt, 0);",
        },
        "_InterlockedExchange_rel": {
            "proto": "long _InterlockedExchange_rel(long volatile * _Target, long);",
            "call": "long tgt = 0; _InterlockedExchange_rel(&tgt, 0);",
        },
        # Exchange (8)
        "_InterlockedExchange8": {
            "proto": "char _InterlockedExchange8(char volatile * _Target, char);",
            "call": "char tgt = 0; _InterlockedExchange8(&tgt, 0);",
        },
        "_InterlockedExchange8_acq": {
            "proto": "char _InterlockedExchange8_acq(char volatile * _Target, char);",
            "call": "char tgt = 0; _InterlockedExchange8_acq(&tgt, 0);",
        },
        "_InterlockedExchange8_nf": {
            "proto": "char _InterlockedExchange8_nf(char volatile * _Target, char);",
            "call": "char tgt = 0; _InterlockedExchange8_nf(&tgt, 0);",
        },
        "_InterlockedExchange8_rel": {
            "proto": "char _InterlockedExchange8_rel(char volatile * _Target, char);",
            "call": "char tgt = 0; _InterlockedExchange8_rel(&tgt, 0);",
        },
        # Exchange (16)
        "_InterlockedExchange16": {
            "proto": "short _InterlockedExchange16(short volatile * _Target, short);",
            "call": "short tgt = 0; _InterlockedExchange16(&tgt, 0);",
        },
        "_InterlockedExchange16_acq": {
            "proto": "short _InterlockedExchange16_acq(short volatile * _Target, short);",
            "call": "short tgt = 0; _InterlockedExchange16_acq(&tgt, 0);",
        },
        "_InterlockedExchange16_nf": {
            "proto": "short _InterlockedExchange16_nf(short volatile * _Target, short);",
            "call": "short tgt = 0; _InterlockedExchange16_nf(&tgt, 0);",
        },
        "_InterlockedExchange16_rel": {
            "proto": "short _InterlockedExchange16_rel(short volatile * _Target, short);",
            "call": "short tgt = 0; _InterlockedExchange16_rel(&tgt, 0);",
        },
        # Exchange (64)
        "_InterlockedExchange64": {
            "proto": "__int64 _InterlockedExchange64(__int64 volatile * _Target, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchange64(&tgt, 0);",
        },
        "_InterlockedExchange64_acq": {
            "proto": "__int64 _InterlockedExchange64_acq(__int64 volatile * _Target, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchange64_acq(&tgt, 0);",
        },
        "_InterlockedExchange64_nf": {
            "proto": "__int64 _InterlockedExchange64_nf(__int64 volatile * _Target, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchange64_nf(&tgt, 0);",
        },
        "_InterlockedExchange64_rel": {
            "proto": "__int64 _InterlockedExchange64_rel(__int64 volatile * _Target, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchange64_rel(&tgt, 0);",
        },
        # ExchangePointer
        "_InterlockedExchangePointer": {
            "proto": "void * _InterlockedExchangePointer(void * volatile * _Target, void *);",
            "call": "void* tgt = 0; _InterlockedExchangePointer(&tgt, 0);",
        },
        "_InterlockedExchangePointer_acq": {
            "proto": "void * _InterlockedExchangePointer_acq(void * volatile * _Target, void *);",
            "call": "void* tgt = 0; _InterlockedExchangePointer_acq(&tgt, 0);",
        },
        "_InterlockedExchangePointer_nf": {
            "proto": "void * _InterlockedExchangePointer_nf(void * volatile * _Target, void *);",
            "call": "void* tgt = 0; _InterlockedExchangePointer_nf(&tgt, 0);",
        },
        "_InterlockedExchangePointer_rel": {
            "proto": "void * _InterlockedExchangePointer_rel(void * volatile * _Target, void *);",
            "call": "void* tgt = 0; _InterlockedExchangePointer_rel(&tgt, 0);",
        },
        # ExchangeAdd (long)
        "_InterlockedExchangeAdd": {
            "proto": "long __cdecl _InterlockedExchangeAdd(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedExchangeAdd(&tgt, 0);",
        },
        "_InterlockedExchangeAdd_acq": {
            "proto": "long _InterlockedExchangeAdd_acq(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedExchangeAdd_acq(&tgt, 0);",
        },
        "_InterlockedExchangeAdd_nf": {
            "proto": "long _InterlockedExchangeAdd_nf(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedExchangeAdd_nf(&tgt, 0);",
        },
        "_InterlockedExchangeAdd_rel": {
            "proto": "long _InterlockedExchangeAdd_rel(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedExchangeAdd_rel(&tgt, 0);",
        },
        # ExchangeAdd (8)
        "_InterlockedExchangeAdd8": {
            "proto": "char _InterlockedExchangeAdd8(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedExchangeAdd8(&tgt, 0);",
        },
        "_InterlockedExchangeAdd8_acq": {
            "proto": "char _InterlockedExchangeAdd8_acq(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedExchangeAdd8_acq(&tgt, 0);",
        },
        "_InterlockedExchangeAdd8_nf": {
            "proto": "char _InterlockedExchangeAdd8_nf(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedExchangeAdd8_nf(&tgt, 0);",
        },
        "_InterlockedExchangeAdd8_rel": {
            "proto": "char _InterlockedExchangeAdd8_rel(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedExchangeAdd8_rel(&tgt, 0);",
        },
        # ExchangeAdd (16)
        "_InterlockedExchangeAdd16": {
            "proto": "short _InterlockedExchangeAdd16(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedExchangeAdd16(&tgt, 0);",
        },
        "_InterlockedExchangeAdd16_acq": {
            "proto": "short _InterlockedExchangeAdd16_acq(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedExchangeAdd16_acq(&tgt, 0);",
        },
        "_InterlockedExchangeAdd16_nf": {
            "proto": "short _InterlockedExchangeAdd16_nf(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedExchangeAdd16_nf(&tgt, 0);",
        },
        "_InterlockedExchangeAdd16_rel": {
            "proto": "short _InterlockedExchangeAdd16_rel(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedExchangeAdd16_rel(&tgt, 0);",
        },
        # ExchangeAdd (64)
        "_InterlockedExchangeAdd64": {
            "proto": "__int64 _InterlockedExchangeAdd64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchangeAdd64(&tgt, 0);",
        },
        "_InterlockedExchangeAdd64_acq": {
            "proto": "__int64 _InterlockedExchangeAdd64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchangeAdd64_acq(&tgt, 0);",
        },
        "_InterlockedExchangeAdd64_nf": {
            "proto": "__int64 _InterlockedExchangeAdd64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchangeAdd64_nf(&tgt, 0);",
        },
        "_InterlockedExchangeAdd64_rel": {
            "proto": "__int64 _InterlockedExchangeAdd64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedExchangeAdd64_rel(&tgt, 0);",
        },
        # Increment (long)
        "_InterlockedIncrement": {
            "proto": "long __cdecl _InterlockedIncrement(long volatile *);",
            "call": "long tgt = 0; _InterlockedIncrement(&tgt);",
        },
        "_InterlockedIncrement_acq": {
            "proto": "long _InterlockedIncrement_acq(long volatile *);",
            "call": "long tgt = 0; _InterlockedIncrement_acq(&tgt);",
        },
        "_InterlockedIncrement_nf": {
            "proto": "long _InterlockedIncrement_nf(long volatile *);",
            "call": "long tgt = 0; _InterlockedIncrement_nf(&tgt);",
        },
        "_InterlockedIncrement_rel": {
            "proto": "long _InterlockedIncrement_rel(long volatile *);",
            "call": "long tgt = 0; _InterlockedIncrement_rel(&tgt);",
        },
        # Increment (16)
        "_InterlockedIncrement16": {
            "proto": "short _InterlockedIncrement16(short volatile *);",
            "call": "short tgt = 0; _InterlockedIncrement16(&tgt);",
        },
        "_InterlockedIncrement16_acq": {
            "proto": "short _InterlockedIncrement16_acq(short volatile *);",
            "call": "short tgt = 0; _InterlockedIncrement16_acq(&tgt);",
        },
        "_InterlockedIncrement16_nf": {
            "proto": "short _InterlockedIncrement16_nf(short volatile *);",
            "call": "short tgt = 0; _InterlockedIncrement16_nf(&tgt);",
        },
        "_InterlockedIncrement16_rel": {
            "proto": "short _InterlockedIncrement16_rel(short volatile *);",
            "call": "short tgt = 0; _InterlockedIncrement16_rel(&tgt);",
        },
        # Increment (64)
        "_InterlockedIncrement64": {
            "proto": "__int64 _InterlockedIncrement64(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedIncrement64(&tgt);",
        },
        "_InterlockedIncrement64_acq": {
            "proto": "__int64 _InterlockedIncrement64_acq(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedIncrement64_acq(&tgt);",
        },
        "_InterlockedIncrement64_nf": {
            "proto": "__int64 _InterlockedIncrement64_nf(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedIncrement64_nf(&tgt);",
        },
        "_InterlockedIncrement64_rel": {
            "proto": "__int64 _InterlockedIncrement64_rel(__int64 volatile *);",
            "call": "__int64 tgt = 0; _InterlockedIncrement64_rel(&tgt);",
        },
        # Or (long)
        "_InterlockedOr": {
            "proto": "long _InterlockedOr(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedOr(&tgt, 0);",
        },
        "_InterlockedOr_acq": {
            "proto": "long _InterlockedOr_acq(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedOr_acq(&tgt, 0);",
        },
        "_InterlockedOr_nf": {
            "proto": "long _InterlockedOr_nf(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedOr_nf(&tgt, 0);",
        },
        "_InterlockedOr_rel": {
            "proto": "long _InterlockedOr_rel(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedOr_rel(&tgt, 0);",
        },
        # Or (8)
        "_InterlockedOr8": {
            "proto": "char _InterlockedOr8(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedOr8(&tgt, 0);",
        },
        "_InterlockedOr8_acq": {
            "proto": "char _InterlockedOr8_acq(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedOr8_acq(&tgt, 0);",
        },
        "_InterlockedOr8_nf": {
            "proto": "char _InterlockedOr8_nf(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedOr8_nf(&tgt, 0);",
        },
        "_InterlockedOr8_rel": {
            "proto": "char _InterlockedOr8_rel(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedOr8_rel(&tgt, 0);",
        },
        # Or (16)
        "_InterlockedOr16": {
            "proto": "short _InterlockedOr16(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedOr16(&tgt, 0);",
        },
        "_InterlockedOr16_acq": {
            "proto": "short _InterlockedOr16_acq(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedOr16_acq(&tgt, 0);",
        },
        "_InterlockedOr16_nf": {
            "proto": "short _InterlockedOr16_nf(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedOr16_nf(&tgt, 0);",
        },
        "_InterlockedOr16_rel": {
            "proto": "short _InterlockedOr16_rel(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedOr16_rel(&tgt, 0);",
        },
        # Or (64)
        "_InterlockedOr64": {
            "proto": "__int64 _InterlockedOr64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedOr64(&tgt, 0);",
        },
        "_InterlockedOr64_acq": {
            "proto": "__int64 _InterlockedOr64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedOr64_acq(&tgt, 0);",
        },
        "_InterlockedOr64_nf": {
            "proto": "__int64 _InterlockedOr64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedOr64_nf(&tgt, 0);",
        },
        "_InterlockedOr64_rel": {
            "proto": "__int64 _InterlockedOr64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedOr64_rel(&tgt, 0);",
        },
        # Xor (long)
        "_InterlockedXor": {
            "proto": "long _InterlockedXor(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedXor(&tgt, 0);",
        },
        "_InterlockedXor_acq": {
            "proto": "long _InterlockedXor_acq(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedXor_acq(&tgt, 0);",
        },
        "_InterlockedXor_nf": {
            "proto": "long _InterlockedXor_nf(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedXor_nf(&tgt, 0);",
        },
        "_InterlockedXor_rel": {
            "proto": "long _InterlockedXor_rel(long volatile *, long);",
            "call": "long tgt = 0; _InterlockedXor_rel(&tgt, 0);",
        },
        # Xor (8)
        "_InterlockedXor8": {
            "proto": "char _InterlockedXor8(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedXor8(&tgt, 0);",
        },
        "_InterlockedXor8_acq": {
            "proto": "char _InterlockedXor8_acq(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedXor8_acq(&tgt, 0);",
        },
        "_InterlockedXor8_nf": {
            "proto": "char _InterlockedXor8_nf(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedXor8_nf(&tgt, 0);",
        },
        "_InterlockedXor8_rel": {
            "proto": "char _InterlockedXor8_rel(char volatile *, char);",
            "call": "char tgt = 0; _InterlockedXor8_rel(&tgt, 0);",
        },
        # Xor (16)
        "_InterlockedXor16": {
            "proto": "short _InterlockedXor16(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedXor16(&tgt, 0);",
        },
        "_InterlockedXor16_acq": {
            "proto": "short _InterlockedXor16_acq(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedXor16_acq(&tgt, 0);",
        },
        "_InterlockedXor16_nf": {
            "proto": "short _InterlockedXor16_nf(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedXor16_nf(&tgt, 0);",
        },
        "_InterlockedXor16_rel": {
            "proto": "short _InterlockedXor16_rel(short volatile *, short);",
            "call": "short tgt = 0; _InterlockedXor16_rel(&tgt, 0);",
        },
        # Xor (64)
        "_InterlockedXor64": {
            "proto": "__int64 _InterlockedXor64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedXor64(&tgt, 0);",
        },
        "_InterlockedXor64_acq": {
            "proto": "__int64 _InterlockedXor64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedXor64_acq(&tgt, 0);",
        },
        "_InterlockedXor64_nf": {
            "proto": "__int64 _InterlockedXor64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedXor64_nf(&tgt, 0);",
        },
        "_InterlockedXor64_rel": {
            "proto": "__int64 _InterlockedXor64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _InterlockedXor64_rel(&tgt, 0);",
        },
    },
    "interlocked_more": {
        "_InterlockedMax64_nf": {
            "proto": "__int64 _InterlockedMax64_nf(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedMax64_nf(arg0, arg1);",
        },
        "_InterlockedUMin8_acq": {
            "proto": "unsigned char _InterlockedUMin8_acq(unsigned char volatile *, unsigned char)",
            "call": "unsigned char volatile * arg0; unsigned char arg1; unsigned char result = _InterlockedUMin8_acq(arg0, arg1);",
        },
        "_InterlockedMax16_nf": {
            "proto": "short _InterlockedMax16_nf(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedMax16_nf(arg0, arg1);",
        },
        "_InterlockedMax_rel": {
            "proto": "long _InterlockedMax_rel(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedMax_rel(arg0, arg1);",
        },
        "_InterlockedNand64_acq": {
            "proto": "__int64 _InterlockedNand64_acq(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedNand64_acq(arg0, arg1);",
        },
        "_InterlockedUMax16_nf": {
            "proto": "unsigned short _InterlockedUMax16_nf(unsigned short volatile *, unsigned short)",
            "call": "unsigned short volatile * arg0; unsigned short arg1; unsigned short result = _InterlockedUMax16_nf(arg0, arg1);",
        },
        "_InterlockedMax_acq": {
            "proto": "long _InterlockedMax_acq(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedMax_acq(arg0, arg1);",
        },
        "_InterlockedNand8_acq": {
            "proto": "char _InterlockedNand8_acq(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedNand8_acq(arg0, arg1);",
        },
        "_InterlockedMax8_nf": {
            "proto": "char _InterlockedMax8_nf(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedMax8_nf(arg0, arg1);",
        },
        "_InterlockedUMin16_nf": {
            "proto": "unsigned short _InterlockedUMin16_nf(unsigned short volatile *, unsigned short)",
            "call": "unsigned short volatile * arg0; unsigned short arg1; unsigned short result = _InterlockedUMin16_nf(arg0, arg1);",
        },
        "_InterlockedMin_nf": {
            "proto": "long _InterlockedMin_nf(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedMin_nf(arg0, arg1);",
        },
        "_InterlockedMax_nf": {
            "proto": "long _InterlockedMax_nf(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedMax_nf(arg0, arg1);",
        },
        "_InterlockedUMax8_nf": {
            "proto": "unsigned char _InterlockedUMax8_nf(unsigned char volatile *, unsigned char)",
            "call": "unsigned char volatile * arg0; unsigned char arg1; unsigned char result = _InterlockedUMax8_nf(arg0, arg1);",
        },
        "_InterlockedMin16_rel": {
            "proto": "short _InterlockedMin16_rel(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedMin16_rel(arg0, arg1);",
        },
        "_InterlockedNand8_rel": {
            "proto": "char _InterlockedNand8_rel(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedNand8_rel(arg0, arg1);",
        },
        "_InterlockedNand64_nf": {
            "proto": "__int64 _InterlockedNand64_nf(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedNand64_nf(arg0, arg1);",
        },
        "_InterlockedNand16_rel": {
            "proto": "short _InterlockedNand16_rel(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedNand16_rel(arg0, arg1);",
        },
        "_InterlockedUMin16_acq": {
            "proto": "unsigned short _InterlockedUMin16_acq(unsigned short volatile *, unsigned short)",
            "call": "unsigned short volatile * arg0; unsigned short arg1; unsigned short result = _InterlockedUMin16_acq(arg0, arg1);",
        },
        "_InterlockedNand16_nf": {
            "proto": "short _InterlockedNand16_nf(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedNand16_nf(arg0, arg1);",
        },
        "_InterlockedUMax_rel": {
            "proto": "unsigned long _InterlockedUMax_rel(unsigned long volatile *, unsigned long)",
            "call": "unsigned long volatile * arg0; unsigned long arg1; unsigned long result = _InterlockedUMax_rel(arg0, arg1);",
        },
        "_InterlockedMax16_rel": {
            "proto": "short _InterlockedMax16_rel(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedMax16_rel(arg0, arg1);",
        },
        "_InterlockedUMin64_acq": {
            "proto": "unsigned __int64 _InterlockedUMin64_acq(unsigned __int64 volatile *, unsigned __int64)",
            "call": "unsigned __int64 volatile * arg0; unsigned __int64 arg1; unsigned __int64 result = _InterlockedUMin64_acq(arg0, arg1);",
        },
        "_InterlockedUMax16_rel": {
            "proto": "unsigned short _InterlockedUMax16_rel(unsigned short volatile *, unsigned short)",
            "call": "unsigned short volatile * arg0; unsigned short arg1; unsigned short result = _InterlockedUMax16_rel(arg0, arg1);",
        },
        "_InterlockedNand8_nf": {
            "proto": "char _InterlockedNand8_nf(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedNand8_nf(arg0, arg1);",
        },
        "_InterlockedUMax64_acq": {
            "proto": "unsigned __int64 _InterlockedUMax64_acq(unsigned __int64 volatile *, unsigned __int64)",
            "call": "unsigned __int64 volatile * arg0; unsigned __int64 arg1; unsigned __int64 result = _InterlockedUMax64_acq(arg0, arg1);",
        },
        "_InterlockedMin64_nf": {
            "proto": "__int64 _InterlockedMin64_nf(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedMin64_nf(arg0, arg1);",
        },
        "_InterlockedUMin16_rel": {
            "proto": "unsigned short _InterlockedUMin16_rel(unsigned short volatile *, unsigned short)",
            "call": "unsigned short volatile * arg0; unsigned short arg1; unsigned short result = _InterlockedUMin16_rel(arg0, arg1);",
        },
        "_InterlockedUMax8_acq": {
            "proto": "unsigned char _InterlockedUMax8_acq(unsigned char volatile *, unsigned char)",
            "call": "unsigned char volatile * arg0; unsigned char arg1; unsigned char result = _InterlockedUMax8_acq(arg0, arg1);",
        },
        "_InterlockedNand_acq": {
            "proto": "long _InterlockedNand_acq(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedNand_acq(arg0, arg1);",
        },
        "_InterlockedNand_rel": {
            "proto": "long _InterlockedNand_rel(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedNand_rel(arg0, arg1);",
        },
        "_InterlockedMin64_acq": {
            "proto": "__int64 _InterlockedMin64_acq(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedMin64_acq(arg0, arg1);",
        },
        "_InterlockedMax64_rel": {
            "proto": "__int64 _InterlockedMax64_rel(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedMax64_rel(arg0, arg1);",
        },
        "_InterlockedMin16_acq": {
            "proto": "short _InterlockedMin16_acq(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedMin16_acq(arg0, arg1);",
        },
        "_InterlockedMax8_rel": {
            "proto": "char _InterlockedMax8_rel(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedMax8_rel(arg0, arg1);",
        },
        "_InterlockedMax64_acq": {
            "proto": "__int64 _InterlockedMax64_acq(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedMax64_acq(arg0, arg1);",
        },
        "_InterlockedNand16_acq": {
            "proto": "short _InterlockedNand16_acq(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedNand16_acq(arg0, arg1);",
        },
        "_InterlockedMin_rel": {
            "proto": "long _InterlockedMin_rel(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedMin_rel(arg0, arg1);",
        },
        "_InterlockedMin_acq": {
            "proto": "long _InterlockedMin_acq(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedMin_acq(arg0, arg1);",
        },
        "_InterlockedUMax8_rel": {
            "proto": "unsigned char _InterlockedUMax8_rel(unsigned char volatile *, unsigned char)",
            "call": "unsigned char volatile * arg0; unsigned char arg1; unsigned char result = _InterlockedUMax8_rel(arg0, arg1);",
        },
        "_InterlockedUMax16_acq": {
            "proto": "unsigned short _InterlockedUMax16_acq(unsigned short volatile *, unsigned short)",
            "call": "unsigned short volatile * arg0; unsigned short arg1; unsigned short result = _InterlockedUMax16_acq(arg0, arg1);",
        },
        "_InterlockedUMin_acq": {
            "proto": "unsigned long _InterlockedUMin_acq(unsigned long volatile *, unsigned long)",
            "call": "unsigned long volatile * arg0; unsigned long arg1; unsigned long result = _InterlockedUMin_acq(arg0, arg1);",
        },
        "_InterlockedNand64_rel": {
            "proto": "__int64 _InterlockedNand64_rel(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedNand64_rel(arg0, arg1);",
        },
        "_InterlockedUMin64_rel": {
            "proto": "unsigned __int64 _InterlockedUMin64_rel(unsigned __int64 volatile *, unsigned __int64)",
            "call": "unsigned __int64 volatile * arg0; unsigned __int64 arg1; unsigned __int64 result = _InterlockedUMin64_rel(arg0, arg1);",
        },
        "_InterlockedMax8_acq": {
            "proto": "char _InterlockedMax8_acq(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedMax8_acq(arg0, arg1);",
        },
        "_InterlockedUMin_rel": {
            "proto": "unsigned long _InterlockedUMin_rel(unsigned long volatile *, unsigned long)",
            "call": "unsigned long volatile * arg0; unsigned long arg1; unsigned long result = _InterlockedUMin_rel(arg0, arg1);",
        },
        "_InterlockedUMax_acq": {
            "proto": "unsigned long _InterlockedUMax_acq(unsigned long volatile *, unsigned long)",
            "call": "unsigned long volatile * arg0; unsigned long arg1; unsigned long result = _InterlockedUMax_acq(arg0, arg1);",
        },
        "_InterlockedMin8_rel": {
            "proto": "char _InterlockedMin8_rel(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedMin8_rel(arg0, arg1);",
        },
        "_InterlockedMin8_acq": {
            "proto": "char _InterlockedMin8_acq(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedMin8_acq(arg0, arg1);",
        },
        "_InterlockedUMin64_nf": {
            "proto": "unsigned __int64 _InterlockedUMin64_nf(unsigned __int64 volatile *, unsigned __int64)",
            "call": "unsigned __int64 volatile * arg0; unsigned __int64 arg1; unsigned __int64 result = _InterlockedUMin64_nf(arg0, arg1);",
        },
        "_InterlockedUMax64_rel": {
            "proto": "unsigned __int64 _InterlockedUMax64_rel(unsigned __int64 volatile *, unsigned __int64)",
            "call": "unsigned __int64 volatile * arg0; unsigned __int64 arg1; unsigned __int64 result = _InterlockedUMax64_rel(arg0, arg1);",
        },
        "_InterlockedMin16_nf": {
            "proto": "short _InterlockedMin16_nf(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedMin16_nf(arg0, arg1);",
        },
        "_InterlockedUMax_nf": {
            "proto": "unsigned long _InterlockedUMax_nf(unsigned long volatile *, unsigned long)",
            "call": "unsigned long volatile * arg0; unsigned long arg1; unsigned long result = _InterlockedUMax_nf(arg0, arg1);",
        },
        "_InterlockedNand_nf": {
            "proto": "long _InterlockedNand_nf(long volatile *, long)",
            "call": "long volatile * arg0; long arg1; long result = _InterlockedNand_nf(arg0, arg1);",
        },
        "_InterlockedUMin_nf": {
            "proto": "unsigned long _InterlockedUMin_nf(unsigned long volatile *, unsigned long)",
            "call": "unsigned long volatile * arg0; unsigned long arg1; unsigned long result = _InterlockedUMin_nf(arg0, arg1);",
        },
        "_InterlockedMax16_acq": {
            "proto": "short _InterlockedMax16_acq(short volatile *, short)",
            "call": "short volatile * arg0; short arg1; short result = _InterlockedMax16_acq(arg0, arg1);",
        },
        "_InterlockedUMin8_rel": {
            "proto": "unsigned char _InterlockedUMin8_rel(unsigned char volatile *, unsigned char)",
            "call": "unsigned char volatile * arg0; unsigned char arg1; unsigned char result = _InterlockedUMin8_rel(arg0, arg1);",
        },
        "_InterlockedMin64_rel": {
            "proto": "__int64 _InterlockedMin64_rel(__int64 volatile *, __int64)",
            "call": "__int64 volatile * arg0; __int64 arg1; __int64 result = _InterlockedMin64_rel(arg0, arg1);",
        },
        "_InterlockedUMax64_nf": {
            "proto": "unsigned __int64 _InterlockedUMax64_nf(unsigned __int64 volatile *, unsigned __int64)",
            "call": "unsigned __int64 volatile * arg0; unsigned __int64 arg1; unsigned __int64 result = _InterlockedUMax64_nf(arg0, arg1);",
        },
        "_InterlockedMin8_nf": {
            "proto": "char _InterlockedMin8_nf(char volatile *, char)",
            "call": "char volatile * arg0; char arg1; char result = _InterlockedMin8_nf(arg0, arg1);",
        },
        "_InterlockedUMin8_nf": {
            "proto": "unsigned char _InterlockedUMin8_nf(unsigned char volatile *, unsigned char)",
            "call": "unsigned char volatile * arg0; unsigned char arg1; unsigned char result = _InterlockedUMin8_nf(arg0, arg1);",
        },
    },
    # BitTest Interlocked builtins list
    "bittest": {
        "_interlockedbittestandreset": {
            "proto": "unsigned char _interlockedbittestandreset(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandreset(&tgt, 0);",
        },
        "_interlockedbittestandreset_acq": {
            "proto": "unsigned char _interlockedbittestandreset_acq(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandreset_acq(&tgt, 0);",
        },
        "_interlockedbittestandreset_nf": {
            "proto": "unsigned char _interlockedbittestandreset_nf(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandreset_nf(&tgt, 0);",
        },
        "_interlockedbittestandreset_rel": {
            "proto": "unsigned char _interlockedbittestandreset_rel(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandreset_rel(&tgt, 0);",
        },
        "_interlockedbittestandreset64": {
            "proto": "unsigned char _interlockedbittestandreset64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandreset64(&tgt, 0);",
        },
        "_interlockedbittestandreset64_acq": {
            "proto": "unsigned char _interlockedbittestandreset64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandreset64_acq(&tgt, 0);",
        },
        "_interlockedbittestandreset64_nf": {
            "proto": "unsigned char _interlockedbittestandreset64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandreset64_nf(&tgt, 0);",
        },
        "_interlockedbittestandreset64_rel": {
            "proto": "unsigned char _interlockedbittestandreset64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandreset64_rel(&tgt, 0);",
        },
        "_interlockedbittestandset": {
            "proto": "unsigned char _interlockedbittestandset(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandset(&tgt, 0);",
        },
        "_interlockedbittestandset_acq": {
            "proto": "unsigned char _interlockedbittestandset_acq(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandset_acq(&tgt, 0);",
        },
        "_interlockedbittestandset_nf": {
            "proto": "unsigned char _interlockedbittestandset_nf(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandset_nf(&tgt, 0);",
        },
        "_interlockedbittestandset_rel": {
            "proto": "unsigned char _interlockedbittestandset_rel(long volatile *, long);",
            "call": "long tgt = 0; _interlockedbittestandset_rel(&tgt, 0);",
        },
        "_interlockedbittestandset64": {
            "proto": "unsigned char _interlockedbittestandset64(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandset64(&tgt, 0);",
        },
        "_interlockedbittestandset64_acq": {
            "proto": "unsigned char _interlockedbittestandset64_acq(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandset64_acq(&tgt, 0);",
        },
        "_interlockedbittestandset64_nf": {
            "proto": "unsigned char _interlockedbittestandset64_nf(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandset64_nf(&tgt, 0);",
        },
        "_interlockedbittestandset64_rel": {
            "proto": "unsigned char _interlockedbittestandset64_rel(__int64 volatile *, __int64);",
            "call": "__int64 tgt = 0; _interlockedbittestandset64_rel(&tgt, 0);",
        },
    },
    "arm64intr_extra": {
        "__sb": {"proto": "void __sb ( void )", "call": "__sb();"},
        "__ld64b": {
            "proto": "void __ld64b ( const void * _addr , unsigned __int64 _value [ 8 ] )",
            "call": "void* _addr = 0;\nunsigned long long _value[1] = {0};\n__ld64b(_addr, _value);",
        },
        "__st64b": {
            "proto": "void __st64b ( void * _addr , unsigned __int64 _value [ 8 ] )",
            "call": "void* _addr = 0;\nunsigned long long _value[1] = {0};\n__st64b(_addr, _value);",
        },
        "__st64bv": {
            "proto": "unsigned __int64 __st64bv ( void * _addr , unsigned __int64 _value [ 8 ] )",
            "call": "void* _addr = 0;\nunsigned long long _value[1] = {0};\n__st64bv(_addr, _value);",
        },
        "__st64bv0": {
            "proto": "unsigned __int64 __st64bv0 ( void * _addr , unsigned __int64 _value [ 8 ] )",
            "call": "void* _addr = 0;\nunsigned long long _value[1] = {0};\n__st64bv0(_addr, _value);",
        },
        "__arm_ld64b": {
            "proto": "static __forceinline data512_t __arm_ld64b ( const void * _addr )",
            "call": "void* _addr = 0;\n__arm_ld64b(_addr);",
            "arch": "+ls64",
        },
        "__arm_st64b": {
            "proto": "static __forceinline void __arm_st64b ( void * _addr , data512_t _value )",
            "call": "void* _addr = 0;\ndata512_t _value = { 0 };\n__arm_st64b(_addr, _value);",
            "arch": "+ls64",
        },
        "__arm_st64bv": {
            "proto": "static __forceinline unsigned __int64 __arm_st64bv ( void * _addr , data512_t _value )",
            "call": "void* _addr = 0;\ndata512_t _value = { 0 };\n__arm_st64bv(_addr, _value);",
            "arch": "+ls64",
        },
        "__arm_st64bv0": {
            "proto": "static __forceinline unsigned __int64 __arm_st64bv0 ( void * _addr , data512_t _value )",
            "call": "void* _addr = 0;\ndata512_t _value = { 0 };\n__arm_st64bv0(_addr, _value);",
            "arch": "+ls64",
        },
        "__load_acquire8": {
            "proto": "unsigned __int8 __load_acquire8 ( const volatile unsigned __int8 * _Target )",
            "call": "unsigned char _Target = 0;\n__load_acquire8(&_Target);",
        },
        "__load_acquire16": {
            "proto": "unsigned __int16 __load_acquire16 ( const volatile unsigned __int16 * _Target )",
            "call": "unsigned short _Target = 0;\n__load_acquire16(&_Target);",
        },
        "__load_acquire32": {
            "proto": "unsigned __int32 __load_acquire32 ( const volatile unsigned __int32 * _Target )",
            "call": "unsigned int _Target = 0;\n__load_acquire32(&_Target);",
        },
        "__load_acquire64": {
            "proto": "unsigned __int64 __load_acquire64 ( const volatile unsigned __int64 * _Target )",
            "call": "unsigned long long _Target = 0;\n__load_acquire64(&_Target);",
        },
        "__ldxr8": {
            "proto": "unsigned __int8 __ldxr8 ( const volatile unsigned __int8 * _Target )",
            "call": "unsigned char _Target = 0;\n__ldxr8(&_Target);",
        },
        "__ldxr16": {
            "proto": "unsigned __int16 __ldxr16 ( const volatile unsigned __int16 * _Target )",
            "call": "unsigned short _Target = 0;\n__ldxr16(&_Target);",
        },
        "__ldxr32": {
            "proto": "unsigned __int32 __ldxr32 ( const volatile unsigned __int32 * _Target )",
            "call": "unsigned int _Target = 0;\n__ldxr32(&_Target);",
        },
        "__ldxr64": {
            "proto": "unsigned __int64 __ldxr64 ( const volatile unsigned __int64 * _Target )",
            "call": "unsigned long long _Target = 0;\n__ldxr64(&_Target);",
        },
        "__ldaxr8": {
            "proto": "unsigned __int8 __ldaxr8 ( const volatile unsigned __int8 * _Target )",
            "call": "unsigned char _Target = 0;\n__ldaxr8(&_Target);",
        },
        "__ldaxr16": {
            "proto": "unsigned __int16 __ldaxr16 ( const volatile unsigned __int16 * _Target )",
            "call": "unsigned short _Target = 0;\n__ldaxr16(&_Target);",
        },
        "__ldaxr32": {
            "proto": "unsigned __int32 __ldaxr32 ( const volatile unsigned __int32 * _Target )",
            "call": "unsigned int _Target = 0;\n__ldaxr32(&_Target);",
        },
        "__ldaxr64": {
            "proto": "unsigned __int64 __ldaxr64 ( const volatile unsigned __int64 * _Target )",
            "call": "unsigned long long _Target = 0;\n__ldaxr64(&_Target);",
        },
        "__stxr8": {
            "proto": "unsigned __int8 __stxr8 ( volatile unsigned __int8 * _Target , unsigned __int8 _Value )",
            "call": "unsigned char _Target = 0;\nunsigned char _Value = 0;\n__stxr8(&_Target, _Value);",
        },
        "__stxr16": {
            "proto": "unsigned __int8 __stxr16 ( volatile unsigned __int16 * _Target , unsigned __int16 _Value )",
            "call": "unsigned short _Target = 0;\nunsigned short _Value = 0;\n__stxr16(&_Target, _Value);",
        },
        "__stxr32": {
            "proto": "unsigned __int8 __stxr32 ( volatile unsigned __int32 * _Target , unsigned __int32 _Value )",
            "call": "unsigned int _Target = 0;\nunsigned int _Value = 0;\n__stxr32(&_Target, _Value);",
        },
        "__stxr64": {
            "proto": "unsigned __int8 __stxr64 ( volatile unsigned __int64 * _Target , unsigned __int64 _Value )",
            "call": "unsigned long long _Target = 0;\nunsigned long long _Value = 0;\n__stxr64(&_Target, _Value);",
        },
        "__stlxr8": {
            "proto": "unsigned __int8 __stlxr8 ( volatile unsigned __int8 * _Target , unsigned __int8 _Value )",
            "call": "unsigned char _Target = 0;\nunsigned char _Value = 0;\n__stlxr8(&_Target, _Value);",
        },
        "__stlxr16": {
            "proto": "unsigned __int8 __stlxr16 ( volatile unsigned __int16 * _Target , unsigned __int16 _Value )",
            "call": "unsigned short _Target = 0;\nunsigned short _Value = 0;\n__stlxr16(&_Target, _Value);",
        },
        "__stlxr32": {
            "proto": "unsigned __int8 __stlxr32 ( volatile unsigned __int32 * _Target , unsigned __int32 _Value )",
            "call": "unsigned int _Target = 0;\nunsigned int _Value = 0;\n__stlxr32(&_Target, _Value);",
        },
        "__stlxr64": {
            "proto": "unsigned __int8 __stlxr64 ( volatile unsigned __int64 * _Target , unsigned __int64 _Value )",
            "call": "unsigned long long _Target = 0;\nunsigned long long _Value = 0;\n__stlxr64(&_Target, _Value);",
        },
        "__clrex": {
            "proto": "void __clrex ( unsigned __int8 crm )",
            "call": "unsigned char crm = 0;\n__clrex(crm);",
        },
        "__ldtr8": {
            "proto": "unsigned __int8 __ldtr8 ( const volatile unsigned __int8 * _Target )",
            "call": "unsigned char _Target = 0;\n__ldtr8(&_Target);",
        },
        "__ldtr16": {
            "proto": "unsigned __int16 __ldtr16 ( const volatile unsigned __int16 * _Target )",
            "call": "unsigned short _Target = 0;\n__ldtr16(&_Target);",
        },
        "__ldtr32": {
            "proto": "unsigned __int32 __ldtr32 ( const volatile unsigned __int32 * _Target )",
            "call": "unsigned int _Target = 0;\n__ldtr32(&_Target);",
        },
        "__ldtr64": {
            "proto": "unsigned __int64 __ldtr64 ( const volatile unsigned __int64 * _Target )",
            "call": "unsigned long long _Target = 0;\n__ldtr64(&_Target);",
        },
        "__ldtrs8": {
            "proto": "signed __int8 __ldtrs8 ( const volatile __int8 * _Target )",
            "call": "char _Target = 0;\n__ldtrs8(&_Target);",
        },
        "__ldtrs16": {
            "proto": "signed __int16 __ldtrs16 ( const volatile __int16 * _Target )",
            "call": "short _Target = 0;\n__ldtrs16(&_Target);",
        },
        "__ldtrs32": {
            "proto": "signed __int32 __ldtrs32 ( const volatile __int32 * _Target )",
            "call": "int _Target = 0;\n__ldtrs32(&_Target);",
        },
        "__sttr8": {
            "proto": "void __sttr8 ( volatile unsigned __int8 * _Target , unsigned __int8 _Value )",
            "call": "unsigned char _Target = 0;\nunsigned char _Value = 0;\n__sttr8(&_Target, _Value);",
        },
        "__sttr16": {
            "proto": "void __sttr16 ( volatile unsigned __int16 * _Target , unsigned __int16 _Value )",
            "call": "unsigned short _Target = 0;\nunsigned short _Value = 0;\n__sttr16(&_Target, _Value);",
        },
        "__sttr32": {
            "proto": "void __sttr32 ( volatile unsigned __int32 * _Target , unsigned __int32 _Value )",
            "call": "unsigned int _Target = 0;\nunsigned int _Value = 0;\n__sttr32(&_Target, _Value);",
        },
        "__sttr64": {
            "proto": "void __sttr64 ( volatile unsigned __int64 * _Target , unsigned __int64 _Value )",
            "call": "unsigned long long _Target = 0;\nunsigned long long _Value = 0;\n__sttr64(&_Target, _Value);",
        },
        "__xpaci": {
            "proto": "void * __xpaci ( void * _Pointer )",
            "call": "void* _Pointer = 0;\n__xpaci(_Pointer);",
        },
        "__rbit": {
            "proto": "unsigned __int32 __rbit ( unsigned __int32 _Value )",
            "call": "unsigned int _Value = 0;\n__rbit(_Value);",
        },
        "__rbitl": {
            "proto": "unsigned long __rbitl ( unsigned long _Value )",
            "call": "unsigned long _Value = 0;\n__rbitl(_Value);",
        },
        "__rbitll": {
            "proto": "unsigned __int64 __rbitll ( unsigned __int64 _Value )",
            "call": "unsigned long long _Value = 0;\n__rbitll(_Value);",
        },
        "__rndr": {
            "proto": "int __rndr ( unsigned __int64 * _adr )",
            "call": "unsigned long long _adr = 0;\n__rndr(&_adr);",
        },
        "__rndrrs": {
            "proto": "int __rndrrs ( unsigned __int64 * _adr )",
            "call": "unsigned long long _adr = 0;\n__rndrrs(&_adr);",
        },
    },
}
