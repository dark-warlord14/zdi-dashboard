# ZDI-09-037: Microsoft Internet Explorer Concurrent Ajax Request Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-037
- **ZDI-CAN:** ZDI-CAN-426
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1528
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-037/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific vulnerability exist due to improper AJAX request synchronization in Internet Explorer. When many asynchronous XMLHttpRequest are running concurrently memory corruption can occur that could be remotely exploited by a malicious attacker.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-019.mspx

## Disclosure Timeline

- 2009-01-15 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
