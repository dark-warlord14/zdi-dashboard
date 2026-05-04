# ZDI-18-137: Hewlett Packard Enterprise Intelligent Management Center RMI Registry Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-137
- **ZDI-CAN:** ZDI-CAN-4824
- **Date:** 2018-01-25
- **CVE:** CVE-2017-5792
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-137/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the euplat RMI registry. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of the Administrator.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03815en_us

## Disclosure Timeline

- 2017-05-17 - Vulnerability reported to vendor
- 2018-01-25 - Coordinated public release of advisory
- 2018-01-25 - Advisory Updated
