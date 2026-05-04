# ZDI-25-325: Hewlett Packard Enterprise Insight Remote Support processAttachmentDataStream Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-325
- **ZDI-CAN:** ZDI-CAN-25954
- **Date:** 2025-06-05
- **CVE:** CVE-2025-37099
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Insight Remote Support
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-325/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Insight Remote Support. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the processAttachmentDataStream method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04878en_us&docLocale=en_US

## Disclosure Timeline

- 2025-02-21 - Vulnerability reported to vendor
- 2025-06-05 - Coordinated public release of advisory
- 2025-06-05 - Advisory Updated
