# ZDI-17-767: Trend Micro Mobile Security for Enterprise widgetforsecurity talker Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-767
- **ZDI-CAN:** ZDI-CAN-4671
- **Date:** 2017-09-15
- **CVE:** CVE-2017-14080
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprise
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-767/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Mobile Security for Enterprise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the initialization of the users table in the tmwf database. When processing an attempt to login a user by an email address, the system can bypass password authentication. An attacker can leverage this vulnerability to escalate privileges to those of an authenticated user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1118224

## Disclosure Timeline

- 2017-05-17 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
