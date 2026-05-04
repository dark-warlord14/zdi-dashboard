# ZDI-07-042: Ipswitch IMail Server GetIMailHostEntry Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-042
- **ZDI-CAN:** ZDI-CAN-166
- **Date:** 2007-07-19
- **CVE:** CVE-2007-2795
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-042/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Ipswitch IMail and ICS server. Authentication is not required to exploit this vulnerability. The specific flaw resides in IMailsec.dll while attempting to authenticate users. The affected component is used by multiple services that listen on a default installation. The authentication mechanism copies user-supplied data into fixed length heap buffers using the lstrcpyA() function. The unbounded copy operation can cause a memory corruption resulting in an exploitable condition.

## Additional Details

Ipswitch has issued an update to correct this vulnerability. More details can be found at: http://www.ipswitch.com/support/imail/releases/im200621.asp

## Disclosure Timeline

- 2007-02-26 - Vulnerability reported to vendor
- 2007-07-19 - Coordinated public release of advisory
