# ZDI-11-018: Oracle Database and Enterprise Manager Grid Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-018
- **ZDI-CAN:** ZDI-CAN-735
- **Date:** 2011-01-18
- **CVE:** CVE-2010-3600
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Database Server
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-018/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Database 11g. Authentication is not required to exploit this vulnerability. The specific flaw exists within a JSP script exposed via an HTTPS server running by default on TCP port 1158. The script allows clients to upload XML files to the server. However, if a NULL byte is supplied within a POST parameter during a request to this JSP page, the process will fail to properly append the XML extension to the created file. An attacker can abuse this to upload executable code which can later be accessed remotely allowing for code execution to be achieved on the server system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2010-04-06 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory
