# ZDI-09-018: Symantec Multiple Product Intel Alert Originator Service Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-018
- **ZDI-CAN:** ZDI-CAN-226
- **Date:** 2009-04-28
- **CVE:** CVE-2009-1430
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec, Symantec, Symantec
- **Affected Products:** AntiVirus Corporate Edition, Client Security, Endpoint Protection
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-018/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec AntiVirus Corporate Edition, Symantec Client Security and Symantec Endpoint Protection. Authentication is not required to exploit this vulnerability. The specific flaw resides in the Alert Originator service, iao.exe, which listens by default on TCP port 38292. The process blindly copies user-supplied data to a stack buffer via a memcpy call. By supplying a specially crafted packet, an attacker can overflow that buffer leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2009&suid=20090428_02

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2009-04-28 - Coordinated public release of advisory
