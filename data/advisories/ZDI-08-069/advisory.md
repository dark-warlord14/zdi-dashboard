# ZDI-08-069: Microsoft Internet Explorer componentFromPoint Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-069
- **ZDI-CAN:** ZDI-CAN-353
- **Date:** 2008-10-14
- **CVE:** CVE-2008-3475
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 6
- **Credit:** Ivan Fratric, http://ifsec.blogspot.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-069/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the componentFromPoint() method exposed through JavaScript. A problem in the implementation of this method for a particular object can be used to arbitrarily control memory access. By exploiting this an attacker can gain access to the target system under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-058.mspx

## Disclosure Timeline

- 2008-06-25 - Vulnerability reported to vendor
- 2008-10-14 - Coordinated public release of advisory
