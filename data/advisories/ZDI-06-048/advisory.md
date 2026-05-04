# ZDI-06-048: Microsoft Internet Explorer normalize() Function Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-048
- **ZDI-CAN:** ZDI-CAN-072
- **Date:** 2006-12-12
- **CVE:** CVE-2006-5581
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 6
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-048/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific vulnerability exists due to improper handling of the normalize() function. When called in certain circumstances user controllable memory can be used to execute arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-072.mspx

## Disclosure Timeline

- 2006-08-31 - Vulnerability reported to vendor
- 2006-12-12 - Coordinated public release of advisory
