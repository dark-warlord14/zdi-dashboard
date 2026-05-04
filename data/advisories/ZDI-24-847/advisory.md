# ZDI-24-847: (Pwn2Own) Alpine Halo9 Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-847
- **ZDI-CAN:** ZDI-CAN-23246
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23962
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Alpine
- **Affected Products:** Halo9
- **Credit:** Le Tran Hai Tung
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-847/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Alpine Halo9 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DLT interface, which listens on TCP port 3490 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device.

## Additional Details

Alpine conducted a Threat Assessment and Remediation Analysis (TARA) in accordance with ISO21434, and concluded that the vulnerability is classified as "Sharing the Risk". Alpine states that they will continue to use the current software without a releasing patch.

## Disclosure Timeline

- 2024-02-01 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
