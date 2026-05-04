# ZDI-09-060: Symantec Multiple Product Intel Alert Originator Service Command Execution Vulnerabilty

## Metadata

- **ZDI ID:** ZDI-09-060
- **ZDI-CAN:** ZDI-CAN-174
- **Date:** 2009-04-28
- **CVE:** CVE-2009-1429
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec, Symantec, Symantec
- **Affected Products:** AntiVirus Corporate Edition, Client Security, Endpoint Protection
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-060/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec AntiVirus Corporate Edition, Symantec Client Security and Symantec Endpoint Protection. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Intel LANDesk Common Base Agent bundled with the affected products. When a specially crafted packet is sent to TCP port 12174, the contents of the packet are passed directly to a call to CreateProcessA() as the lpCommandLine argument. The resulting command will be executed with SYSTEM privileges.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2009&suid=20090428_02

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2009-04-28 - Coordinated public release of advisory
