# ZDI-11-028: Symantec AMS Intel Alert Service AMSSendAlertAct Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-028
- **ZDI-CAN:** ZDI-CAN-528
- **Date:** 2011-01-27
- **CVE:** CVE-2010-0110
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Alert Management System
- **Credit:** Anonymous Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Alert Management System. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AMSLIB.dll module while processing data sent from the msgsys.exe process which listens by default on TCP port 38292. The DLL allocates a fixed length stack buffer and subsequently copies a user-supplied string using memcpy without validating the size. By supplying a large enough value this buffer can be overflowed leading to arbitrary code execution under the context of the vulnerable daemon.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110126_00

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2011-01-27 - Coordinated public release of advisory
