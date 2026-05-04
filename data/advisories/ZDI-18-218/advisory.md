# ZDI-18-218: Trend Micro Smart Protection Server Auth Command Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-218
- **ZDI-CAN:** ZDI-CAN-5625
- **Date:** 2018-02-28
- **CVE:** CVE-2018-6231
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Smart Protection Server
- **Credit:** Alain Homewood (Insomnia Security)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-218/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Trend Micro Smart Protection Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of credentials provided at login. When parsing the username, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119385

## Disclosure Timeline

- 2018-02-02 - Vulnerability reported to vendor
- 2018-02-28 - Coordinated public release of advisory
- 2018-02-28 - Advisory Updated
