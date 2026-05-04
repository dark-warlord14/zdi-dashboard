# ZDI-19-1038: Hewlett Packard Enterprise Intelligent Management Center UrlAccessController Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1038
- **ZDI-CAN:** ZDI-CAN-8943
- **Date:** 2020-01-29
- **CVE:** CVE-2020-24629
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1038/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Hewlett Packard Enterprise Intelligent Management Center. The specific flaw exists within the UrlAccessController servlet. The issue results from the lack of proper filtering of URLs. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=a00093539en_us

## Disclosure Timeline

- 2019-08-09 - Vulnerability reported to vendor
- 2020-01-29 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
