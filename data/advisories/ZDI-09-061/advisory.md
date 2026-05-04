# ZDI-09-061: Symantec Multiple Product Intel Alert Originator Service Invalid Length Check Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-061
- **ZDI-CAN:** ZDI-CAN-246
- **Date:** 2009-04-28
- **CVE:** CVE-2009-1430
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec, Symantec, Symantec
- **Affected Products:** Endpoint Protection, Client Security, AntiVirus Corporate Edition
- **Credit:** Sebastian Apelt (sebastian.apelt@siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-061/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec AntiVirus Corporate Edition, Symantec Client Security and Symantec Endpoint Protection. Authentication is not required to exploit this vulnerability. The specific flaws are exposed via the MsgSys.exe process that listens by default on TCP port 38929. This process forwards requests to the Intel Originator Service (ioa.exe) process. The iao.exe process fails to validate length specifiers within the request in several locations leading to stack based buffer overflows. The overflows occurring during calls to strcpy and memcpy leading to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2009&suid=20090428_02

## Disclosure Timeline

- 2007-11-07 - Vulnerability reported to vendor
- 2009-04-28 - Coordinated public release of advisory
