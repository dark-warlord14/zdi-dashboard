# ZDI-24-1631: Hewlett Packard Enterprise AutoPass License Server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1631
- **ZDI-CAN:** ZDI-CAN-24691
- **Date:** 2024-12-02
- **CVE:** CVE-2024-51767
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** AutoPass License Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1631/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Hewlett Packard Enterprise AutoPass License Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 5814 by default. The issue results from making an authorization decision based on a non-canonical URL. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04760en_us&docLocale=en_US

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-12-02 - Coordinated public release of advisory
- 2024-12-02 - Advisory Updated
