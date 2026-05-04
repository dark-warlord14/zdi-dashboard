# ZDI-19-291: Drupal File file_create_filename Persistent Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-291
- **ZDI-CAN:** ZDI-CAN-7246
- **Date:** 2019-03-26
- **CVE:** CVE-2019-6341
- **CVSS:** 6.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
- **Affected Vendors:** Drupal
- **Affected Products:** Drupal 8
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Drupal. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the filename parameter provided to the file.inc component. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the web server.

## Additional Details

Drupal has issued an update to correct this vulnerability. More details can be found at: https://www.drupal.org/sa-core-2019-004

## Disclosure Timeline

- 2018-09-19 - Vulnerability reported to vendor
- 2019-03-26 - Coordinated public release of advisory
