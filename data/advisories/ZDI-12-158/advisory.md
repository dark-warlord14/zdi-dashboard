# ZDI-12-158: Microsoft Internet Explorer MSADO CacheSize Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-158
- **ZDI-CAN:** ZDI-CAN-1521
- **Date:** 2012-08-22
- **CVE:** CVE-2012-1891
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 9
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the MSADO component. When handling the a user specified CacheSize property the process uses this value to calculate the 'real' cache size. This value is used without proper validation. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser. This bug is a failed fix for CVE-2011-0027 / http://www.zerodayinitiative.com/advisories/ZDI-11-002/

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-045

## Disclosure Timeline

- 2012-02-13 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
