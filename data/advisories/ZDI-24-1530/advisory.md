# ZDI-24-1530: WordPress Core maybe_unserialize Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1530
- **ZDI-CAN:** ZDI-CAN-22613
- **Date:** 2024-11-19
- **CVE:** CVE-2024-31210
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WordPress
- **Affected Products:** Core
- **Credit:** @_s_n_t of @pentestltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1530/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WordPress Core. Authentication may be required to exploit this vulnerability, depending on the product configuration. The specific flaw exists within the maybe_unserialize function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

WordPress has issued an update to correct this vulnerability. More details can be found at: https://wordpress.org/documentation/wordpress-version/version-6-4-3/

## Disclosure Timeline

- 2024-01-10 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
