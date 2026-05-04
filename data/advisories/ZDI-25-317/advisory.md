# ZDI-25-317: Hewlett Packard Enterprise StoreOnce VSA deletePackages Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-317
- **ZDI-CAN:** ZDI-CAN-25314
- **Date:** 2025-06-02
- **CVE:** CVE-2025-37094
- **CVSS:** 5.5
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** StoreOnce VSA
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-317/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Hewlett Packard Enterprise StoreOnce VSA. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the deletePackages method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbst04847en_us&docLocale=en_US

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-06-02 - Coordinated public release of advisory
- 2025-06-02 - Advisory Updated
