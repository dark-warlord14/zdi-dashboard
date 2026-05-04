# ZDI-07-074: Microsoft Internet Explorer Node Manipulation Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-074
- **ZDI-CAN:** ZDI-CAN-189
- **Date:** 2007-12-11
- **CVE:** CVE-2007-3903
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-074/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The flaw exists due to improper use of the "cloneNode" and "nodeValue" javascript functions. When a specially crafted element is used during a repetitive call to one of these functions memory corruption can occur leading to remote code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-069.mspx

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2007-12-11 - Coordinated public release of advisory
