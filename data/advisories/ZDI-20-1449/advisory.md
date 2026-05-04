# ZDI-20-1449: Hewlett Packard Enterprise Systems Insight Manager AMF Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1449
- **ZDI-CAN:** ZDI-CAN-11847
- **Date:** 2020-12-18
- **CVE:** CVE-2020-7200
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Systems Insight Manager
- **Credit:** Harrison Neal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1449/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Systems Insight Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the AMF protocol. Crafted data in an AMF protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=hpesbgn04068en_us

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2020-12-18 - Coordinated public release of advisory
