# ZDI-16-478: Siemens SINEMA Server Insecure File Permissions Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-478
- **ZDI-CAN:** ZDI-CAN-3662
- **Date:** 2016-08-17
- **CVE:** CVE-2016-6486
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Siemens
- **Affected Products:** SINEMA Server
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-478/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Siemens SINEMA Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of the product. The executables for new system services are stored in directories for which all users have full control allowing for new executables to be swapped for the system service executables. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-215-02

## Disclosure Timeline

- 2016-04-05 - Vulnerability reported to vendor
- 2016-08-17 - Coordinated public release of advisory
