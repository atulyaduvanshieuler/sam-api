#level ={table_name: [(name of foreign key in table_name,
#                       corresponding table to which this foreign key belongs)]}


level1={
    'vehicles':[('biw', 'biws'), ('power_train', 'powertrains'), ('semi_sprung_assembly', 'semi_sprung_assemblies'), ('rear_suspension_assembly', 'rear_suspension_assemblies'), ('driveshaft_assembly', 'driveshaft_assemblies'), ('fork_and_suspension_assembly', 'fork_and_suspension_assemblies'), ('disc_brake_assembly', 'disc_brake_assemblies'), ('rear_wheel_assembly', 'rear_wheel_assemblies'), ('front_wheel_assembly', 'front_wheel_assemblies'), ('brake_pedal_assembly', 'brake_pedal_assemblies'), ('vehicle_harness', 'vehicle_harnesses'), ('mark', 'marks'), ('battery_assembly', 'battery_assemblies'), ('cocktail_box_assembly', 'cocktail_box_assemblies'), ('telematics', 'telematics'), ('load_body', 'load_bodies')]
    }


sub_assembly_column_table_relations={
    'cocktail_box_assemblies':[('cocktail_box', 'cocktail_boxes'), ('aux_battery', 'aux_batteries'), ('motor_controller', 'motor_controllers'), ('on_board_charger', 'on_board_chargers'), ('dc_dc', 'dc_dcs'), ('stark', 'starks'), ('arc_reactor_assembly', 'arc_reactor_assemblies')],
    'battery_assemblies':[('cell', 'cells'), ('bms', 'bmses'), ('battery', 'batteries'), ('battery_box', 'battery_boxes'), ('signal_connector', 'signal_connectors')],
    'brake_pedal_assemblies':[('tmc', 'tmcs'), ('reservoir', 'reservoirs'), ('brake_switch', 'brake_switches')],
    'front_wheel_assemblies':[('tyre', 'tyres'), ('rim', 'rims')],
    'rear_wheel_assemblies':[('tyre', 'tyres'), ('rim', 'rims')],
    'disc_brake_assemblies':[('rotor', 'rotors'), ('caliper', 'calipers')],
    'fork_and_suspension_assemblies':[('upper_and_lower_cone', 'upper_and_lower_cones'), ('fork_2_bearing', 'fork_2_bearings'), ('bottom_link', 'bottom_links'), ('spring', 'springs'), ('strut', 'struts')],
    'driveshaft_assemblies':[('rear_axle', 'rear_axles'), ('crown_nut', 'crown_nuts')],
    'rear_suspension_assemblies':[('spring', 'springs'), ('strut', 'struts'), ('mounting_rubber', 'mounting_rubbers')],
    'semi_sprung_assemblies':[('trailing_arm', 'trailing_arms'), ('drum', 'drums'), ('brake_plate', 'brake_plates'), ('hub_assembly', 'hub_assemblies')],
    'powertrains':[('gearbox', 'gearboxes'), ('motor', 'motors'), ('muff_cup', 'muff_cups')]
    }

subassembly_component_tables={'cocktail_boxes': 'cocktail_box_assemblies', 'aux_batteries': 'cocktail_box_assemblies', 'motor_controllers': 'cocktail_box_assemblies', 'on_board_chargers': 'cocktail_box_assemblies', 'dc_dcs': 'cocktail_box_assemblies', 'starks': 'cocktail_box_assemblies', 'arc_reactor_assemblies': 'cocktail_box_assemblies', 'cells': 'battery_assemblies', 'bmses': 'battery_assemblies', 'batteries': 'battery_assemblies', 'battery_boxes': 'battery_assemblies', 'signal_connectors': 'battery_assemblies', 'tmcs': 'brake_pedal_assemblies', 'reservoirs': 'brake_pedal_assemblies', 'brake_switches': 'brake_pedal_assemblies', 'tyres': 'rear_wheel_assemblies', 'rims': 'rear_wheel_assemblies', 'rotors': 'disc_brake_assemblies', 'calipers': 'disc_brake_assemblies', 'upper_and_lower_cones': 'fork_and_suspension_assemblies', 'fork_2_bearings': 'fork_and_suspension_assemblies', 'bottom_links': 'fork_and_suspension_assemblies', 'springs': 'rear_suspension_assemblies', 'struts': 'rear_suspension_assemblies', 'rear_axles': 'driveshaft_assemblies', 'crown_nuts': 'driveshaft_assemblies', 'mounting_rubbers': 'rear_suspension_assemblies', 'trailing_arms': 'semi_sprung_assemblies', 'drums': 'semi_sprung_assemblies', 'brake_plates': 'semi_sprung_assemblies', 'hub_assemblies': 'semi_sprung_assemblies', 'gearboxes': 'powertrains', 'motors': 'powertrains', 'muff_cups': 'powertrains'}

vehicles_column_table_relation={'biws': 'biw', 'powertrains': 'power_train', 'semi_sprung_assemblies': 'semi_sprung_assembly', 'rear_suspension_assemblies': 'rear_suspension_assembly', 'driveshaft_assemblies': 'driveshaft_assembly', 'fork_and_suspension_assemblies': 'fork_and_suspension_assembly', 'disc_brake_assemblies': 'disc_brake_assembly', 'rear_wheel_assemblies': 'rear_wheel_assembly', 'front_wheel_assemblies': 'front_wheel_assembly', 'brake_pedal_assemblies': 'brake_pedal_assembly', 'vehicle_harnesses': 'vehicle_harness', 'marks': 'mark', 'battery_assemblies': 'battery_assembly', 'cocktail_box_assemblies': 'cocktail_box_assembly', 'telematics': 'telematics', 'load_bodies': 'load_body'}
#need to change bettery_id later on also need to change fork_2_bearing
component_tables_and_their_ids={'cocktail_boxes': 'cocktail_box_id', 'aux_batteries': 'aux_battery_id', 'motor_controllers': 'motor_controller_id', 'on_board_chargers': 'on_board_charger_id', 'dc_dcs': 'dc_dc_id', 'starks': 'stark_id', 'arc_reactor_assemblies': 'arc_reactor_assembly_id', 'cells': 'cell_id', 'bmses': 'bms_id', 'batteries': 'bettery_id', 'battery_boxes': 'battery_box_id', 'signal_connectors': 'signal_connector_id', 'tmcs': 'tmc_id', 'reservoirs': 'reservoir_id', 'brake_switches': 'brake_switch_id', 'tyres': 'tyre_id', 'rims': 'rim_id', 'rotors': 'rotor_id', 'calipers': 'caliper_id', 'upper_and_lower_cones': 'upper_and_lower_cone_id', 'fork_2_bearings': 'for_2_bearing_id', 'bottom_links': 'bottom_link_id', 'springs': 'spring_id', 'struts': 'strut_id', 'rear_axles': 'rear_axle_id', 'crown_nuts': 'crown_nut_id', 'mounting_rubbers': 'mounting_rubber_id', 'trailing_arms': 'trailing_arm_id', 'drums': 'drum_id', 'brake_plates': 'brake_plate_id', 'hub_assemblies': 'hub_assembly_id', 'gearboxes': 'gearbox_id', 'motors': 'motor_id', 'muff_cups': 'muff_cup_id'}

frontend_backend_component_table={'cocktail_box': 'cocktail_boxes', 'aux_battery': 'aux_batteries', 'motor_controller': 'motor_controllers', 'on_board_charger': 'on_board_chargers', 'dc_dc': 'dc_dcs', 'stark': 'starks', 'arc_reactor_assembly': 'arc_reactor_assemblies', 'cell': 'cells', 'bms': 'bmses', 'battery': 'batteries', 'battery_box': 'battery_boxes', 'signal_connector': 'signal_connectors', 'tmc': 'tmcs', 'reservoir': 'reservoirs', 'brake_switch': 'brake_switches', 'front_tyre': 'tyres', 'front_rim': 'rims', 'rear_tyre': 'tyres', 'rear_rim': 'rims', 'rotor': 'rotors', 'caliper': 'calipers', 'upper_and_lower_cone': 'upper_and_lower_cones', 'fork_2_bearing': 'fork_2_bearings', 'bottom_link': 'bottom_links', 'fork_and_suspension_assembly_spring': 'springs', 'fork_and_suspension_assembly_strut': 'struts', 'rear_axle': 'rear_axles', 'crown_nut': 'crown_nuts', 'rear_suspension_assembly_spring': 'springs', 'rear_suspension_assembly_strut': 'struts', 'mounting_rubber': 'mounting_rubbers', 'trailing_arm': 'trailing_arms', 'drum': 'drums', 'brake_plate': 'brake_plates', 'hub_assembly': 'hub_assemblies', 'gearbox': 'gearboxes', 'motor': 'motors', 'muff_cup': 'muff_cups'}

frontend_backend_subassembly_table={'cocktail_box': 'cocktail_box_assemblies', 'aux_battery': 'cocktail_box_assemblies', 'motor_controller': 'cocktail_box_assemblies', 'on_board_charger': 'cocktail_box_assemblies', 'dc_dc': 'cocktail_box_assemblies', 'stark': 'cocktail_box_assemblies', 'arc_reactor_assembly': 'cocktail_box_assemblies', 'cell': 'battery_assemblies', 'bms': 'battery_assemblies', 'battery': 'battery_assemblies', 'battery_box': 'battery_assemblies', 'signal_connector': 'battery_assemblies', 'tmc': 'brake_pedal_assemblies', 'reservoir': 'brake_pedal_assemblies', 'brake_switch': 'brake_pedal_assemblies', 'front_tyre': 'front_wheel_assemblies', 'front_rim': 'front_wheel_assemblies', 'rear_tyre': 'rear_wheel_assemblies', 'rear_rim': 'rear_wheel_assemblies', 'rotor': 'disc_brake_assemblies', 'caliper': 'disc_brake_assemblies', 'upper_and_lower_cone': 'fork_and_suspension_assemblies', 'fork_2_bearing': 'fork_and_suspension_assemblies', 'bottom_link': 'fork_and_suspension_assemblies', 'fork_and_suspension_assembly_spring': 'fork_and_suspension_assemblies', 'fork_and_suspension_assembly_strut': 'fork_and_suspension_assemblies', 'rear_axle': 'driveshaft_assemblies', 'crown_nut': 'driveshaft_assemblies', 'rear_suspension_assembly_spring': 'rear_suspension_assemblies', 'rear_suspension_assembly_strut': 'rear_suspension_assemblies', 'mounting_rubber': 'rear_suspension_assemblies', 'trailing_arm': 'semi_sprung_assemblies', 'drum': 'semi_sprung_assemblies', 'brake_plate': 'semi_sprung_assemblies', 'hub_assembly': 'semi_sprung_assemblies', 'gearbox': 'powertrains', 'motor': 'powertrains', 'muff_cup': 'powertrains'}

frontend_backend_subassembly_table_columns={'cocktail_box': 'cocktail_box', 'aux_battery': 'aux_battery', 'motor_controller': 'motor_controller', 'on_board_charger': 'on_board_charger', 'dc_dc': 'dc_dc', 'stark': 'stark', 'arc_reactor_assembly': 'arc_reactor_assembly', 'cell': 'cell', 'bms': 'bms', 'battery': 'battery', 'battery_box': 'battery_box', 'signal_connector': 'signal_connector', 'tmc': 'tmc', 'reservoir': 'reservoir', 'brake_switch': 'brake_switch', 'front_tyre': 'tyre', 'front_rim': 'rim', 'rear_tyre': 'tyre', 'rear_rim': 'rim', 'rotor': 'rotor', 'caliper': 'caliper', 'upper_and_lower_cone': 'upper_and_lower_cone', 'fork_2_bearing': 'fork_2_bearing', 'bottom_link': 'bottom_link', 'fork_and_suspension_assembly_spring': 'spring', 'fork_and_suspension_assembly_strut': 'strut', 'rear_axle': 'rear_axle', 'crown_nut': 'crown_nut', 'rear_suspension_assembly_spring': 'spring', 'rear_suspension_assembly_strut': 'strut', 'mounting_rubber': 'mounting_rubber', 'trailing_arm': 'trailing_arm', 'drum': 'drum', 'brake_plate': 'brake_plate', 'hub_assembly': 'hub_assembly', 'gearbox': 'gearbox', 'motor': 'motor', 'muff_cup': 'muff_cup'}

