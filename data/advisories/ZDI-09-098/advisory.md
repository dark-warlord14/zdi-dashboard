# ZDI-09-098: Symantec Multiple Products VRTSweb.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-098
- **ZDI-CAN:** ZDI-CAN-456
- **Date:** 2009-12-09
- **CVE:** CVE-2009-3027
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec, Symantec, Symantec, Symantec, Symantec
- **Affected Products:** Symantec Backup Exec Continuous Protection Server, Veritas NetBackup, Veritas Storage Foundation, Veritas Cluster Server, Veritas CommandCentral Storage
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of multiple Symantec products. Authentication is not required to exploit this vulnerability. The specific flaw exists within the VRTSweb.exe Web Server component which listens by default on TCP ports 8181, 8443, and 14300. The process fails to properly validate an authentication request made to port 14300. By providing a specific request an attacker can bypass the authentication and instruct the process to unpack and execute data within an arbitrary WAR file. This can be leveraged to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2009&suid=20091209_00

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-12-09 - Coordinated public release of advisory
