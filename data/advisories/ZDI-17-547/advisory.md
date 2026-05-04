# ZDI-17-547: (0Day) Advantech WebAccess nvA1Media Brightness Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-547
- **ZDI-CAN:** ZDI-CAN-4069
- **Date:** 2017-08-07
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-547/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within nvA1Media.ocx. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/08/2016, 11/09/2016, 11/10/2016 and 11/15/2016 - ZDI disclosed the reports, 44 in all, to ICS-CERT 11/09/2016 - The vendor acknowledged receipt of the report through ICS-CERT and ICS-CERT provided ICS-VU-714103 04/27/2017 - ICS-CERT notified ZDI these might be fixed in the latest version and asked would ZDI re-test 05/03/2017 - ZDI replied that we cannot do the testing for Advantech ICS-CERT did not respond 06/23/2017 - ZDI wrote to ICS-CERT requesting any available update 07/31/2017 - ZDI wrote to ICS-CERT requesting any available update 08/01/2017 - ZDI wrote to ICS-CERT advising of the intent to 0-day -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\E19E79EC-F62E-40A0-952D-E49AEC7BEC2F If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2016-11-08 - Vulnerability reported to vendor
- 2017-08-07 - Coordinated public release of advisory
