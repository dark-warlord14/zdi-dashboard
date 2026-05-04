# ZDI-11-156: Sybase M-Business Anywhere agd.exe username Parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-156
- **ZDI-CAN:** ZDI-CAN-1089
- **Date:** 2011-05-09
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sybase
- **Affected Products:** MBusiness Anywhere
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-156/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sybase M-Business Anywhere. Authentication is not required to exploit this vulnerability. The specific flaw exists within agsync.dll, which listens for SOAP and sync (HTTP) requests on ports 80 and 443 (HTTPS). When handling a supplied username parameter the process fails to verify the string length. This user-supplied data is then copied to a static sized buffer on the heap. A remote attacker could use this flaw to inject arbitrary code into the agd.exe process, which runs by default under the SYSTEM context.

## Additional Details

Sybase has issued an update to correct this vulnerability. More details can be found at: http://www.sybase.com/detail?id=1093029

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-05-09 - Coordinated public release of advisory
