# ZDI-07-051: Trend Micro ServerProtect TMregChange() Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-051
- **ZDI-CAN:** ZDI-CAN-217
- **Date:** 2007-09-07
- **CVE:** CVE-2007-4731
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Server Protect. Authentication is not required to exploit this vulnerability. The specific flaw exists within the routine TMregChange() exported by TMReg.dll which is reachable through the custom protocol subcode "\x15\x00\x00\x00". The TCP socket bound to port 5005 receives user-supplied data which is copied without proper bounds checking to a stack-based buffer. Thereby resulting in an exploitable condition.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://www.trendmicro.com/ftp/documentation/readme/spnt_558_win_en_securitypatch4_readme.txt

## Disclosure Timeline

- 2007-07-17 - Vulnerability reported to vendor
- 2007-09-07 - Coordinated public release of advisory
