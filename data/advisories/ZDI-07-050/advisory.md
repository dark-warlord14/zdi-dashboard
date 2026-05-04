# ZDI-07-050: Trend Micro ServerProtect RPCFN_SetComputerName() Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-050
- **ZDI-CAN:** ZDI-CAN-215
- **Date:** 2007-09-07
- **CVE:** CVE-2007-4218
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro ServerProtect. Authentication is not required to exploit this vulnerability. The specific flaw is exposed through the RPC interface bound on TCP port 5168 and defined in SpntSvc.exe with the following UUID: 25288888-bd5b-11d1-9d53-0080c83a5c2c The vulnerable function, RPCFN_SetComputerName(), is reached when the custom protocols "subcode" is set to "\x30\x00\x0a\x00". Improper use of the MultiByteToWideChar() API results in an exploitable stack based buffer overflow.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://www.trendmicro.com/ftp/documentation/readme/spnt_558_win_en_securitypatch4_readme.txt

## Disclosure Timeline

- 2007-07-17 - Vulnerability reported to vendor
- 2007-09-07 - Coordinated public release of advisory
