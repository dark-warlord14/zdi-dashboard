# ZDI-08-024: Symantec Altiris Deployment Solution SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-024
- **ZDI-CAN:** ZDI-CAN-290
- **Date:** 2008-05-15
- **CVE:** CVE-2008-2286
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Altiris Deployment Solution
- **Credit:** Brett Moore of Insomnia Security www.insomniasec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-024/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Symantec Altiris Deployment Solution. User interaction is not required to exploit this vulnerability. The specific flaw exists within the axengine.exe process listening by default on TCP port 402. A lack of proper sanitation while parsing requests allows for a remote attacker to inject arbitrary SQL statements into the database. Exploitation of this vulnerability can result in arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2008.05.14a.html

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-05-15 - Coordinated public release of advisory
