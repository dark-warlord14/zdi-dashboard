# ZDI-12-012: (0Day) McAfee SaaS myCIOScn.dll ShowReport Method Remote Command Execution

## Metadata

- **ZDI ID:** ZDI-12-012
- **ZDI-CAN:** ZDI-CAN-1094
- **Date:** 2012-01-12
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** McAfee
- **Affected Products:** Security-as-a-Service
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of McAfee Security-as-a-Service. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaws exists within myCIOScn.dll. MyCioScan.Scan.ShowReport() will accept commands that are passed to a function that simply executes them without authentication. This can be leveraged by a malicious attacker to execute arbitrary code within the context of the browser.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibilty Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\209EBDEE-065C-11D4-A6B8-00C04F0D38B7 If the Compatibility Flags value is set to 0x00000400 the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2012-01-12 - Coordinated public release of advisory
