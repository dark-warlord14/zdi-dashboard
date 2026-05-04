# ZDI-15-461: Solarwinds Log and Event Manager Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-461
- **ZDI-CAN:** ZDI-CAN-2730
- **Date:** 2015-10-07
- **CVE:** CVE-2015-7839
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Log and Event Manager
- **Credit:** Matt Molinyawe - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-461/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Solarwinds Log and Event Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within requests to /services/messagebroker/nonsecurestreamingamf utilizing the traceroute functionality. A command injection vulnerability exists which allows an attacker to execute arbitrary commands on all managed computers using the LEM agent connected to the Log and Event Manager. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the agent application.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/lem/docs/releasenotes/releasenotes.htm Resolved in LEM 6.2 release

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-10-07 - Coordinated public release of advisory
