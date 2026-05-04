# ZDI-14-303: SolarWinds Log and Event Manager Static Credential Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-303
- **ZDI-CAN:** ZDI-CAN-2154
- **Date:** 2014-09-03
- **CVE:** CVE-2014-5504
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Log and Event Manager
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-303/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Log and Event Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the usage of HyperSQL. The issue lies in the usage of static credentials to access the database. A remote attacker can use this vulnerability to execute code under the context of the database.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/lem/docs/releasenotes/releasenotes.htm

## Disclosure Timeline

- 2014-02-18 - Vulnerability reported to vendor
- 2014-09-03 - Coordinated public release of advisory
