# ZDI-19-130: Drupal Phar File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-130
- **ZDI-CAN:** ZDI-CAN-7232
- **Date:** 2019-01-25
- **CVE:** CVE-2019-6339
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Drupal
- **Affected Products:** Drupal 8
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-130/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Drupal. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of Phar archives. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the web server.

## Additional Details

Drupal has issued an update to correct this vulnerability. More details can be found at: https://www.drupal.org/sa-core-2019-002

## Disclosure Timeline

- 2018-09-10 - Vulnerability reported to vendor
- 2019-01-25 - Coordinated public release of advisory
