# ZDI-18-001: Hewlett Packard Enterprise Moonshot Provisioning Manager Appliance khuploadfile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-001
- **ZDI-CAN:** ZDI-CAN-4944
- **Date:** 2018-01-03
- **CVE:** CVE-2017-8976
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Moonshot Provisioning Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Moonshot Provisioning Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the khuploadfile.cgi file. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03803en_us

## Disclosure Timeline

- 2017-06-27 - Vulnerability reported to vendor
- 2018-01-03 - Coordinated public release of advisory
