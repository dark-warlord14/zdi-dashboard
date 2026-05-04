# ZDI-07-077: Trend Micro ServerProtect StRpcSrv.dll Insecure Method Exposure Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-077
- **ZDI-CAN:** ZDI-CAN-157
- **Date:** 2007-12-17
- **CVE:** CVE-2007-6507
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Eric DETOISIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-077/
## Vulnerability Details

These vulnerabilities allow attackers to execute arbitrary code on vulnerable installations of Trend Micro ServerProtect. Authentication is not required to exploit these vulnerabilities. The specific flaw exists in the SpntSvc.exe daemon, bound by default on TCP port 5168 and exposing the following DCE/RPC interface through TmRpcSrv.dll: /* opcode: 0x00, address: 0x65741030 */ error_status_t sub_65741030 ( [in] handle_t arg_1, [in] long arg_2, [in][size_is(arg_4)] byte arg_3[], [in] long arg_4, [out][size_is(arg_6)] byte arg_5[], [in] long arg_6 ); Various sub-functions from StRpcSrv.dll are exposed in this interface and allow for full file system access that can be trivially leveraged to executed arbitrary code.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://www.trendmicro.com/ftp/documentation/readme/spnt_558_win_en_securitypatch4_readme.txt

## Disclosure Timeline

- 2007-02-01 - Vulnerability reported to vendor
- 2007-12-17 - Coordinated public release of advisory
