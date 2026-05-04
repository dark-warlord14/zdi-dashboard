# ZDI-24-416: Centreon sysName Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-416
- **ZDI-CAN:** ZDI-CAN-20731
- **Date:** 2024-04-29
- **CVE:** CVE-2023-51633
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** Andreas Finstad
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-416/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Centreon. User interaction is required to exploit this vulnerability. The specific flaw exists within the processing of the sysName OID in SNMP. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in Centreon-web versions 22.10.15, 23.04.10 and 23.10.1 https://github.com/centreon/centreon/pull/2464

## Disclosure Timeline

- 2023-06-07 - Vulnerability reported to vendor
- 2024-04-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
