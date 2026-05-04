# ZDI-24-1632: Hewlett Packard Enterprise AutoPass License Server hsqldb Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1632
- **ZDI-CAN:** ZDI-CAN-24692
- **Date:** 2024-12-02
- **CVE:** CVE-2024-51768
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** AutoPass License Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1632/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise AutoPass License Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the hsqldb service, which listens on TCP port 9001 by default. The issue results from using a vulnerable third party component. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04760en_us&docLocale=en_US

## Disclosure Timeline

- 2024-07-18 - Vulnerability reported to vendor
- 2024-12-02 - Coordinated public release of advisory
- 2024-12-02 - Advisory Updated
