# ZDI-21-337: Hewlett Packard Enterprise Network Orchestrator uaf-token SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-337
- **ZDI-CAN:** ZDI-CAN-12187
- **Date:** 2021-03-18
- **CVE:** CVE-2021-26578
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Network Orchestrator
- **Credit:** Erik de Jong
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-337/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise Network Orchestrator. Authentication is not required to exploit this vulnerability. The specific flaw exists within the connections resource. A crafted uaf-token header can trigger execution of SQL queries composed from a user-supplied string. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04097en_us

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-03-18 - Coordinated public release of advisory
