# ZDI-18-1289: OMRON Industrial Automation CX-Supervisor CSNewDataSets Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1289
- **ZDI-CAN:** ZDI-CAN-6612
- **Date:** 2018-10-17
- **CVE:** CVE-2018-17913
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-Supervisor
- **Credit:** Ariele Caltabiano (kimiya) of 9SG Security Team - kimiya@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1289/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PAG files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-290-01

## Disclosure Timeline

- 2018-07-05 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
