# ZDI-20-1208: Hewlett Packard Enterprise Universal API Framework uaf_token SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1208
- **ZDI-CAN:** ZDI-CAN-11502
- **Date:** 2020-09-21
- **CVE:** CVE-2020-24623
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Universal API Framework
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1208/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise Universal API Framework. Authentication is not required to exploit this vulnerability. The specific flaw exists within the connections resource. A crafted uaf-token header can trigger execution of SQL queries composed from a user-supplied string. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=emr_na-hpesbgn04024en_us

## Disclosure Timeline

- 2020-07-17 - Vulnerability reported to vendor
- 2020-09-21 - Coordinated public release of advisory
