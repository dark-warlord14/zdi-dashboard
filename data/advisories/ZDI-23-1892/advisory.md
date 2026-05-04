# ZDI-23-1892: (0Day) Voltronic Power ViewPower getModbusPassword Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1892
- **ZDI-CAN:** ZDI-CAN-22073
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51587
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Voltronic Power
- **Affected Products:** ViewPower
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1892/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Voltronic Power ViewPower. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getModbusPassword method. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

08/03/23 – ZDI made multiple attempts to contact the vendor across sales, support, and professional networking channels, which yielded no response from the vendor. We also contacted CISA, who was unsuccessful in receiving a response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
