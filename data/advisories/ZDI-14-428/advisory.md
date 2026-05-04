# ZDI-14-428: (0Day) SolarWinds Server and Application Monitor Alert Manager Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-428
- **ZDI-CAN:** ZDI-CAN-2517
- **Date:** 2015-10-05
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Server and Application Monitor
- **Credit:** Tom McCredie - tom.mac@hp.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-428/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of SolarWinds Server and Application Monitor. This vulnerability requires the attacker to have an unprivileged account on the system. The specific flaw exists within the Alert Manager component. Alerts within this component can be configured in a way that allows for the execution of arbitrary scripts or programs. An attacker can leverage this to elevate privileges and execute code in the context of NT Authority\SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch because vendor indicates that the vulnerability does not meet the bar for security servicing. 09/04/2014 - ZDI disclosed to the vendor 09/08/2014 - Vendor indicated 'by design' and that no fix would be forthcoming -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted users.

## Disclosure Timeline

- 2014-09-04 - Vulnerability reported to vendor
- 2015-10-05 - Coordinated public release of advisory
