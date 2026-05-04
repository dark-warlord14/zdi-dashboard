# ZDI-25-034: Ivanti Endpoint Manager AlertService Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-034
- **ZDI-CAN:** ZDI-CAN-25416
- **Date:** 2025-01-19
- **CVE:** CVE-2024-13169
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** Piotr Bazydlo (@chudypb) and Simon Zuckerbraun of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-034/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Ivanti Endpoint Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AlertService. The issue results from an incorrect type cast. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-January-2025-for-EPM-2024-and-EPM-2022-SU6

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
