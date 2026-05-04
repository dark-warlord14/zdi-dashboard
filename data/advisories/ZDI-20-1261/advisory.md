# ZDI-20-1261: Advantech WebAccess/SCADA WADashboard External Control of File Path Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1261
- **ZDI-CAN:** ZDI-CAN-11262
- **Date:** 2020-10-19
- **CVE:** CVE-2020-25161
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/SCADA
- **Credit:** Sivathmican Sivakumaran
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/SCADA. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the WADashboard component. The issue results from the lack of proper validation of a user-supplied path prior to using it to read and execute code from a file. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-289-01

## Disclosure Timeline

- 2020-06-19 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
