# ZDI-14-012: WellinTech KingSCADA KingAlarm & Event KAEManageServer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-012
- **ZDI-CAN:** ZDI-CAN-1553
- **Date:** 2014-02-05
- **CVE:** CVE-2013-2826
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WellinTech
- **Affected Products:** KingAlarm & Event
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WellinTech KingSCADA KingAlarm&Event. Authentication is not required to exploit this vulnerability. The specific flaw exists within KAEManageServer.exe, which listens by default on TCP port 8130. Authentication to this service is performed locally through the KAEClientManager console but no authentication is performed against remote connections. A remote attacker with knowledge of the protocol can use this to disclose certain credentials and login to the Oracle database as a legitimate user.

## Additional Details

WellinTech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-13-344-01

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2014-02-05 - Coordinated public release of advisory
