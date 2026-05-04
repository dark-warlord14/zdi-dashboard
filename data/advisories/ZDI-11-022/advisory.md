# ZDI-11-022: Oracle Business Intelligence emagent.exe nmehl_getURIParams Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-022
- **ZDI-CAN:** ZDI-CAN-835
- **Date:** 2011-01-18
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Business Intelligence One. Authentication is not required to exploit this vulnerability. The flaw exists within the emagent.exe component which listens by default on TCP port 3938. When handling an HTTP request in oranmemso.dll the function nmehl_getURIParams blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

issue was fixed in Oct 2005 CPU: http://www.oracle.com/technetwork/topics/security/cpuoct2005-090497.html Researcher credit for this issue was mentioned in the CPU for Jan 2011: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory
