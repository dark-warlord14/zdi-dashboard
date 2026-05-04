# ZDI-25-183: (0Day) Bdrive NetDrive Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-183
- **ZDI-CAN:** ZDI-CAN-25295
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2769
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bdrive
- **Affected Products:** NetDrive
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-183/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Bdrive NetDrive. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

09/26/24 – ZDI contacted the vendor’s support team via email 11/08/24 – ZDI sent a second PSIRT contact request to Bdrive’s support team 11/12/24 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
