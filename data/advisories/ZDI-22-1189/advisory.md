# ZDI-22-1189: Trend Micro Apex One Origin Validation Error Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1189
- **ZDI-CAN:** ZDI-CAN-16314
- **Date:** 2022-09-14
- **CVE:** CVE-2022-40140
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1189/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT Listener service. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to delete the Security Agent from the endpoint.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000291528

## Disclosure Timeline

- 2022-02-09 - Vulnerability reported to vendor
- 2022-09-14 - Coordinated public release of advisory
