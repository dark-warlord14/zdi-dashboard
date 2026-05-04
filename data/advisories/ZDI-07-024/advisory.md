# ZDI-07-024: Trend Micro ServerProtect EarthAgent Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-024
- **ZDI-CAN:** ZDI-CAN-155
- **Date:** 2007-05-07
- **CVE:** CVE-2007-2508
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Eric DETOISIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-024/
## Vulnerability Details

These vulnerabilities allow attackers to execute arbitrary code on vulnerable installations of Trend Micro ServerProtect. Authentication is not required to exploit these vulnerabilities. The specific flaw exists in the EarthAgent.exe daemon, bound by default on TCP port 3628 and exposing the following DCE/RPC interface through TmRpcSrv.dll: /* opcode: 0x00, address: 0x65741030 */ error_status_t sub_65741030 ( [in] handle_t arg_1, [in] long arg_2, [in][size_is(arg_4)] byte arg_3[], [in] long arg_4, [out][size_is(arg_6)] byte arg_5[], [in] long arg_6 ); A sub-function within this interface is vulnerable to a stack overflow due an unbounded call to wcscpy().

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://www.trendmicro.com/download_beta/product.asp?productid=17

## Disclosure Timeline

- 2007-02-01 - Vulnerability reported to vendor
- 2007-05-07 - Coordinated public release of advisory
