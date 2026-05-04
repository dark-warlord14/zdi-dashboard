# ZDI-10-018: IBM Cognos Server Backdoor Account Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-018
- **ZDI-CAN:** ZDI-CAN-670
- **Date:** 2010-02-18
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Cognos
- **Credit:** AbdulAziz Hariri of Insight Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-018/
## Vulnerability Details

This vulnerability allows remote attackers to execute remote code on vulnerable installations of IBM Cognos Server. Proper authentication is not required to exploit this vulnerability. The specific flaw exists due to a hidden manager-level account with a default password defined in the user configuration of the bundled Tomcat server. This server can be reached via HTTP on TCP port 19300. A malicious attacker can use this account to manage or deploy a servlet onto the server. By abusing this ability a remote attacker can execute arbitrary code under the context of the user running the Tomcat server.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21419065

## Disclosure Timeline

- 2010-01-15 - Vulnerability reported to vendor
- 2010-02-18 - Coordinated public release of advisory
