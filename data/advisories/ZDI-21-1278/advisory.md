# ZDI-21-1278: Hewlett Packard Enterprise iLO Amplifier Pack backup Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1278
- **ZDI-CAN:** ZDI-CAN-14056
- **Date:** 2021-11-05
- **CVE:** CVE-2021-29212
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** iLO Amplifier Pack
- **Credit:** Erik de Jong
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1278/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise iLO Amplifier Pack. Authentication is not required to exploit this vulnerability. The specific flaw exists within the backup endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=emr_na-hpesbgn04189en_us

## Disclosure Timeline

- 2021-07-07 - Vulnerability reported to vendor
- 2021-11-05 - Coordinated public release of advisory
